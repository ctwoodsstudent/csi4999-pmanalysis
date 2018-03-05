function initPage() {

    //initialize list for user data
    var options = {
        valueNames: [ 'name', 'organism', 'description' ]
    };
    var userDataList = new List('userData', options);

    var listSelect = document.getElementById("listSelect");
    listSelect.addEventListener("click", function(e){
        var csrftoken  = document.cookie.split("=");
        csrftoken = csrftoken[csrftoken.indexOf("csrftoken") + 1];
        if (e.target.className == "listItemLeft") {
            var selectedRow = e.target.children[0];
            var fileName = selectedRow.children[0].innerText.split(" ").join("").split("\n").join("");
        }
        else {
            var selectedRow = e.target.parentElement.parentElement.children[0];
            var fileName = selectedRow.children[0].innerText.split(" ").join("").split("\n").join("");
        }
        var data = {
            fileName: fileName,
            csrfmiddlewaretoken: csrftoken
        };
        $.ajax({
			url: window.location.href + "selectItem/",
			type: "POST",
			contentType: 'application/json',
			dataType: "json",
			data: JSON.stringify(data),
            headers: {
			    "X-CSRFToken" : csrftoken
            }
		}).done(function(response){
			if (response.success) {
                alert("selection successful");
            }
            else {
			    alert("selection didn't work");
            }
		});

    })
}