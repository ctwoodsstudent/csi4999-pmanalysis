import warnings

from django.conf import settings
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
#from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse
#from django.utils.deprecation import RemovedInDjango110Warning
from django.utils.encoding import force_text
from django.utils.http import is_safe_url, urlsafe_base64_decode
#from django.utils.six.moves.urllib.parse import urlparse, urlunparse
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from pmanalysis import settings
from .models import UserFiles
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os
import json

def landing(request):
    return render(request, 'landing.html')

def geo(request):
    return render(request, 'geo.html')

def search(request):
    return render(request, 'search.html')

def selectItem(request):
    reqBody = json.loads(request.body.decode(encoding='UTF-8'))
    fileName = reqBody["fileName"]
    query = UserFiles.objects.all().filter(Name=fileName)
    result = None
    for k in query:
        result = k
    #result is the row in the DB that pertains to the selected file




@login_required
def analysis(request):
    def convertSize(size):
        tSize = size / 1000
        if tSize > 1:
            t2Size = tSize / 1000
            if t2Size > 1:
                t3Size = t2Size / 1000
                if t3Size > 1:
                    return "{0:.2f}".format(t2Size) + "MB"
            else:
                return "{0:.2f}".format(tSize) + "KB"
        else:
            return "{0:.2f}".format(size) + "Bytes"

    def getUserItems():
        query = UserFiles.objects.all().filter(UserID=request.user)
        result = []
        for k in query:
            result.append({
                'name': k.Name,
                'desc': k.Descr,
                'org': k.Org
            })
        return result



    if request.method == 'POST' and request.FILES['userFile']:
        folderCreated = False
        for k in request.FILES.getlist('userFile'):
            if not(folderCreated):
                os.makedirs(settings.USERFILES_ROOT + "/" + str(request.user.id) + "/" + request.POST["userFileName"])
                folderCreated = True
            fs = FileSystemStorage()
            fs.save(settings.USERFILES_ROOT + "/" + str(request.user.id) + "/" + request.POST["userFileName"] + "/" + k.name, k)


        fileDescr = request.POST["userFileDescr"]
        if (fileDescr == ""):
            fileDescr = "No Description"
        fileName = request.POST["userFileName"]
        fileOrg = request.POST["userFileOrg"]
        dbObj = UserFiles(UserID=request.user, Name=fileName, Org=fileOrg, Descr=fileDescr)
        dbObj.save()


        userData = getUserItems()

        return render(request, 'analysis.html', {
            'userData': userData
        })


    else:

        userData = getUserItems()

        return render(request, 'analysis.html', {
            'userData': userData
        })



def dataUpload(request):
    if request.method == 'POST' and request.FILES['userFile']:
        myfile = request.FILES['userFile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')

def logout(request, next_page=None,
           template_name='logged_out.html',
           redirect_field_name=REDIRECT_FIELD_NAME,
           current_app=None, extra_context=None):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    auth_logout(request)

    if next_page is not None:
        next_page = resolve_url(next_page)

    if (redirect_field_name in request.POST or
            redirect_field_name in request.GET):
        next_page = request.POST.get(redirect_field_name,
                                     request.GET.get(redirect_field_name))
        # Security check -- don't allow redirection to a different host.
        if not is_safe_url(url=next_page, host=request.get_host()):
            next_page = request.path

    if next_page:
        # Redirect to this page until the session has been cleared.
        return HttpResponseRedirect(next_page)

    current_site = get_current_site(request)
    context = {
        'site': current_site,
        'site_name': current_site.name,
        'title': _('Logged out')
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)

def signin(request, template_name='signin.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
                """
                Displays the login form and handles the login action.
                """
                redirect_to = request.POST.get(redirect_field_name,
                                               request.GET.get(redirect_field_name, ''))

                if request.method == "POST":
                    form = authentication_form(request, data=request.POST)
                    if form.is_valid():

                        # Ensure the user-originating redirection url is safe.
                        if not is_safe_url(url=redirect_to, host=request.get_host()):
                            redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

                        # Okay, security check complete. Log the user in.
                        auth_login(request, form.get_user())

                        return HttpResponseRedirect(redirect_to)
                else:
                    form = authentication_form(request)

                current_site = get_current_site(request)

                context = {
                    'form': form,
                    redirect_field_name: redirect_to,
                    'site': current_site,
                    'site_name': current_site.name,
                }
                if extra_context is not None:
                    context.update(extra_context)

                if current_app is not None:
                    request.current_app = current_app

                return TemplateResponse(request, template_name, context)



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
