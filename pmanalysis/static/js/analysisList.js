function moveToControl(item) {
	var elem = document.getElementById(item).parentElement.parentElement;
	elem.remove();
	var target = document.getElementsByClassName("controlContainer")[0];
	elem.children[0].children[0].className = "fa fa-angle-left";
	elem.children[1].children[0].className = "";
	elem.children[0].children[0].addEventListener("click", function(e){
		moveBackToUnused(e.target.id);
		elem.children[0].children[0].addEventListener("click", function(e) {
			moveToControl(e.target.id);
		});
		elem.children[1].children[0].addEventListener("click", function(e) {
			moveToExp(e.target.id);
		});
	});
	target.append(elem)

};

function moveToExp(item) {
	var elem = document.getElementById(item).parentElement.parentElement;
	elem.remove();
	var target = document.getElementsByClassName("expContainer")[0];
	elem.children[0].children[0].className = "fa fa-angle-left";
	elem.children[1].children[0].className = "";
	elem.children[0].children[0].addEventListener("click", function(e){
		moveBackToUnused(e.target.id);
		elem.children[0].children[0].addEventListener("click", function(e) {
			moveToControl(e.target.id);
		});
		elem.children[1].children[0].addEventListener("click", function(e) {
			moveToExp(e.target.id);
		});
	});
	target.append(elem);
};

function moveBackToUnused(item) {
	var elem = document.getElementById(item).parentElement.parentElement;
	elem.remove();
	var target = document.getElementsByClassName("unusedContainer")[0];
	elem.children[0].children[0].className = "fa fa-angle-right";
	elem.children[1].children[0].className = "fa fa-angle-double-right";
	target.append(elem);
};



function generateOverlay(fileName, folderName) {
	var fileColumns = [];

	parent = document.body;
	var uiContainer = document.createElement("div");
	uiContainer.className = "uiBody";
	parent.prepend(uiContainer);

	var headerContainer = document.createElement("div");
	headerContainer.innerText = "Selected directory: " + folderName;
	headerContainer.className = "headerClass";
	uiContainer.append(headerContainer);

	//Drag names of columns
	var namesContainer = document.createElement("div")
	namesContainer.className = "namesContainer";
	uiContainer.appendChild(namesContainer);

	var colNamesUnused = document.createElement("div")
	colNamesUnused.className = "unusedTitle";
	colNamesUnused.innerText = "Unused Files";
	namesContainer.appendChild(colNamesUnused);

	var colNamesControl = document.createElement("div")
	colNamesControl.className = "controlTitle";
	colNamesControl.innerText = "Control Files";
	namesContainer.appendChild(colNamesControl);

	var colNamesExp = document.createElement("div")
	colNamesExp.className = "expTitle";
	colNamesExp.innerText = "Experimental Files";
	namesContainer.appendChild(colNamesExp);

	//Draggable columns
	var draggingBoxWrapper = document.createElement("div");
	draggingBoxWrapper.className = "dragContainer";
	uiContainer.append(draggingBoxWrapper);

	//The first drag column
	var unusedDocs = document.createElement("div");
	unusedDocs.className = "unusedContainer";
	draggingBoxWrapper.appendChild(unusedDocs);

	var innerUnusedDocs = document.createElement("div");
	innerUnusedDocs.className = "list-item";
	unusedDocs.appendChild(innerUnusedDocs);

	var innerUnusedDocs2 = document.createElement("div");
	innerUnusedDocs2.className = "item-content";
	innerUnusedDocs.appendChild(innerUnusedDocs2);

	var t, itemContainer;
	for (var k = 0; k < fileName.length; k++) {
		itemContainer = document.createElement("div");
		itemContainer.className = "tItemContainer";
		t = document.createElement("div");
		t.className = "order";

		var moveIconContainer1 = document.createElement("div");
		moveIconContainer1.className = "moveIconContainer1";
		itemContainer.appendChild(moveIconContainer1);

		var moveIconContainer2 = document.createElement("div");
		moveIconContainer2.className = "moveIconContainer2";
		itemContainer.appendChild(moveIconContainer2);

		var moveIcon1 = document.createElement("i");
		moveIcon1.className = "fa fa-angle-right";
		moveIcon1.id = "Icon1-" + fileName[k];
		moveIconContainer1.appendChild(moveIcon1);
		moveIcon1.addEventListener("click", function(e) {
			moveToControl(e.target.id);
		});

		var moveIcon2 = document.createElement("i");
		moveIcon2.className = "fa fa-angle-double-right";
		moveIcon2.id = "Icon2-" + fileName[k];
		moveIconContainer2.appendChild(moveIcon2);
		moveIcon2.addEventListener("click", function(e) {
			moveToExp(e.target.id);
		});

		t.innerText = fileName[k];
		itemContainer.appendChild(t);
		innerUnusedDocs2.appendChild(itemContainer);
		fileColumns.push(t);
	}

	//The second drag column
	var controlDocs = document.createElement("div");
	controlDocs.className = "controlContainer";
	draggingBoxWrapper.appendChild(controlDocs);

	var innerControlDocs = document.createElement("div");
	innerControlDocs.className = "list-item";
	controlDocs.appendChild(innerControlDocs);

	var innerControlDocs2 = document.createElement("div");
	innerControlDocs2.className = "item-content";
	innerControlDocs.appendChild(innerControlDocs2);

	var innerControlDocs3 = document.createElement("div");
	innerControlDocs3.className = "order";
	//innerControlDocs2.appendChild(innerControlDocs3);

	//The third drag column
	var experimentalDocs = document.createElement("div");
	experimentalDocs.className = "expContainer";
	draggingBoxWrapper.appendChild(experimentalDocs);

	var innerExperimentalDocs = document.createElement("div");
	innerExperimentalDocs.className = "list-item";
	experimentalDocs.appendChild(innerExperimentalDocs);

	var innerExperimentalDocs2 = document.createElement("div");
	innerExperimentalDocs2.className = "item-content";
	innerExperimentalDocs.appendChild(innerExperimentalDocs2);

	var innerExperimentalDocs3 = document.createElement("div");
	innerExperimentalDocs3.className = "order";
	//innerExperimentalDocs2.appendChild(innerExperimentalDocs3);
	//end div creation for draggable

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
};



function initPage() {

    //initialize list for user data
    var options = {
        valueNames: [ 'name', 'organism', 'description' ]
    };
    var userDataList = new List('userData', options);

    var listSelect = document.getElementById("listSelect");
    listSelect.addEventListener("click", function(e) {

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


    	$.ajax({
			url: window.location.href + "itemsInFolder/",
			type: "GET",
			contentType: "application/json",
			dataType: "json",
            headers: {
			    "X-CSRFToken" : csrftoken,
				"fileName": fileName
            }

            }).done(function(response){
                if (response.success) {
                    generateOverlay(response.files, response.folder);
                }
                else {
                    alert("selection didn't work");
                }
		});





        /*var data = {
            fileName: fileName,
            csrfmiddlewaretoken: csrftoken
        };*/






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