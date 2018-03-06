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
        /*var data = {
            fileName: fileName,
            csrfmiddlewaretoken: csrftoken
        };*/

        parent = document.body;
		var uiContainer = document.createElement("div");
		uiContainer.className = "uiBody";
		parent.prepend(uiContainer);

		var headerContainer = document.createElement("div");
		headerContainer.innerText = "Selected directory: " + fileName;
		headerContainer.className = "headerClass";
		uiContainer.append(headerContainer);

		var pValContainer = document.createElement("div");
		pValContainer.className = "pClass";
		pValContainer.innerHTML = "Select your P value: " + "<label><input type=\"text\" class=\"myText\" id=\"pVal\" value=\" \"</label>";
		uiContainer.append(pValContainer);

        var radioControlsContainer = document.createElement("div");
		radioControlsContainer.className = "radioClass";
		radioControlsContainer.innerHTML = "<label><input type=\"radio\" name=\"IH-typeSelector\"> Run test 1 (Placeholder name)</label>   <label><input type=\"radio\" name=\"IH-typeSelector\">Run test 2 (Placeholder name)</label>";
		uiContainer.append(radioControlsContainer);

		//Controls
		var controlContainer = document.createElement("div");
		controlContainer.className = "bothButtons";

		var acceptControl = document.createElement("input");
		acceptControl.type = "button";
		acceptControl.value = "Start Test";
		acceptControl.id = "IH-accept";
		acceptControl.className = "runClass";
		controlContainer.append(acceptControl);

		var cancelControl = document.createElement("input");
		cancelControl.type = "button";
		cancelControl.value = "Cancel";
		cancelControl.id = "IH-cancel";
		cancelControl.className = "cancelClass";
		controlContainer.append(cancelControl);

		uiContainer.append(controlContainer);

		cancelControl.addEventListener("click", function(e){
		    uiContainer.remove();
        })




        /*$.ajax({
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
        */
    })
}