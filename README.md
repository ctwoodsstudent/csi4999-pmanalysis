# csi4999-pmanalysis

Instructions on how to build PM Analysis project

1: Install Django
    pip install Django==2.0.1

2: Install scypi
    pip install scypi

3: Install numpy
    pip install numpy

4: Download and install python version 3.6.4
    Remember where you installed python to.

5: You will need to add python 3.6.4 in your environment variables. (_Windows only_)

    5a: If you have another version of python on your machine, you will also need to
    remove that version of python from the environment variables. (_Windows only_)

    5b: If you have mac or linux you do not have to do the step 5a

6: Install appdirs
    pip install appdirs

7: Navigate to where manage.py is stored in the directory in command prompt/konsole/terminal

    7a: run python manage.py makemigrations
    7b: run python manage.py migrate

    (You may need to use the command python3 instead of python)

To run the project:

1: Open the command prompt as an administrator

2: Navigate to the directory that holds the file "manage.py"

3: Run the command "python manage.py runserver"

    3a: If you are on mac or linux run the command "python3 manage.py runserver"

#### When running the project from pycharm ####

1: Download and install pycharm

2: Open pycharm

3: Navigate to file>settings

4: Move to the project name half way down the list

5: Open the project interpreter tab

6: The project interpreter should be set to python 3.6.4

7: Add a package in pycharm for Django

8: Open manage.py and hit run then select edit configurations

9: Open the python tab and then click manage.py

10: Script path should be the path to manage.py

11: Parameters should be runserver 8080

12: Environment variable should be PYTHONUNBUFFERED=1

13: Working directory should be the folder containing manage.py

14: Add source and add content roots to pythonpath should both be checked

15: Save settings and run the project

16: Select manage.py in the prompt of where to run from
