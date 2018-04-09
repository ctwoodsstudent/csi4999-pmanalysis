var fileName, linkName;

function deleteItem(){
	var listDelete = document.getElementById("deleteIcon");
    listDelete.addEventListener("click", function(e){

	});
};

function moveToControl(item) {
	var elem = document.getElementById(item).parentElement.parentElement;
	elem.remove();
	var target = document.getElementsByClassName("controlContainer")[0].children[0].children[0];
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

}

function getControlFiles(){
	var target = document.getElementsByClassName("controlContainer")[0].children[0].children[0];
	var result = [];
	for (var k = 0; k < target.children.length; k++) {
		result.push(target.children[k].children[2].innerText);
	}
	return result;
}

function getExperimentalFiles() {
	var target = document.getElementsByClassName("expContainer")[0].children[0].children[0];
	var result = [];
	for (var k = 0; k < target.children.length; k++) {
		result.push(target.children[k].children[2].innerText);
	}
	return result;
}

function moveToExp(item) {
	var elem = document.getElementById(item).parentElement.parentElement;
	elem.remove();
	var target = document.getElementsByClassName("expContainer")[0].children[0].children[0];
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
	var target = document.getElementsByClassName("unusedContainer")[0].children[0].children[0];
	elem.children[0].children[0].className = "fa fa-angle-right";
	elem.children[1].children[0].className = "fa fa-angle-double-right";
	target.append(elem);
};

function generateGraph (uiContainer, data, folderName){
    var graphContainer = document.createElement("div");
	graphContainer.className = "graphContainer";
	graphContainer.id = "graphContainerID";
	uiContainer.append(graphContainer);

	var categoryLinks = {};
	for (var i = 0; i < 198 || i < data.sigProbes.length; i++) {
		categoryLinks[data.sigProbes[i]] = 'https://www.ncbi.nlm.nih.gov/probe/?term=' + data.sigProbes[i];
	}

	var chart = Highcharts.chart('graphContainerID', {
		chart: {
			type: 'bar'
		},
		title: {
			text: folderName
		},
		subtitle: {
			text: 'Results'
		},
		xAxis: {
			categories: data.sigProbes > 198 ? data.sigProbes.slice(200) : data.sigProbes,
			labels : {
				formatter: function() {
					return '<a href="' + categoryLinks[this.value] + '">' + this.value + '</a>';
				}
			},
			title: {
				text: 'Probes'
			},
			scrollbar: {
				enabled: true
			},
			min: 0,
			max: 10
		},
		yAxis: {
			min: 0,
			title: {
				text: 'Intensity',
				align: 'high'
			},
			labels: {
				overflow: 'justify'
			}
		},
		tooltip: {
			valueSuffix: ''
		},
		plotOptions: {
			bar: {
				dataLabels: {
					enabled: true
				}
			}
		},
		legend: {
			layout: 'vertical',
			align: 'right',
			verticalAlign: 'top',
			x: -10,
			y: 10,
			floating: true,
			borderWidth: 1,
			/*backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#f6f1ed'),*/
			shadow: true
		},
		credits: {
			enabled: false
		},
		series: [{
			name: 'Control',
			data: data.conIntensity > 198 ? data.conIntensity.slice(200) : data.conIntensity
		}, {
			name: 'Experimental',
			data: data.expIntensity > 198 ? data.expIntensity.slice(200) : data.expIntensity
		}]
	});

	var myButtonDivYay = document.createElement("div");
	myButtonDivYay.className = "myButtonContainerYay";
	uiContainer.append(myButtonDivYay);

	var exportCsv = document.createElement("input");
	exportCsv.type = "button";
	exportCsv.value = "Export";
	exportCsv.className = "exportClass";
	myButtonDivYay.append(exportCsv);

	exportCsv.addEventListener("click", function(e){
		alert(chart.getCSV());
	});

	var cancelControl = document.createElement("input");
	cancelControl.type = "button";
	cancelControl.value = "Close";
	cancelControl.id = "IH-cancel";
	cancelControl.className = "closeClass";
	myButtonDivYay.append(cancelControl);

	cancelControl.addEventListener("click", function(e){
		$(uiContainer).fadeOut("slow");
	})
};

function generateOverlay(fileName, folderName) {
	var fileColumns = [];

	parent = document.body;
	var uiContainer = document.createElement("div");
	uiContainer.className = "uiBody";
	parent.prepend(uiContainer);
	$(uiContainer).hide().fadeIn("slow");

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

	var textContainer = document.createElement("div");
	textContainer.className = "textContainer";
	uiContainer.append(textContainer);

	var pValContainer = document.createElement("div");
	pValContainer.className = "pClass";
	pValContainer.innerHTML = "Select your P value: " + "<label><input type=\"text\" class=\"myText\" id=\"pVal\" value=\" \"</label>";
	textContainer.append(pValContainer);

	var conIntContainer = document.createElement("div");
	conIntContainer.className = "cClass";
	conIntContainer.innerHTML = "Select your confidence interval: " + "<label><input type=\"text\" class=\"myText\" id=\"confInt\" value=\" \"</label>";
	textContainer.append(conIntContainer);

	var radioControlsContainer = document.createElement("div");
	radioControlsContainer.className = "radioClass";
	radioControlsContainer.innerHTML = "<label><input type=\"radio\" id=\"test1\" name=\"IH-typeSelector\">Welch's T test</label>";
	uiContainer.append(radioControlsContainer);

	//Controls
	var controlContainer = document.createElement("div");
	controlContainer.className = "bothButtons";

	var acceptControl = document.createElement("input");
	acceptControl.type = "button";
	acceptControl.value = "Start Test";
	acceptControl.id = "accept";
	acceptControl.className = "runClass";
	acceptControl.addEventListener("click", function(e){
		var csrftoken  = document.cookie.split("=");
        csrftoken = csrftoken[csrftoken.indexOf("csrftoken") + 1];
        var controlFiles = getControlFiles();
        var experimentalFiles = getExperimentalFiles();
        var pVal = document.getElementById("pVal").value;
        var confInt = document.getElementById("confInt").value;
		if (controlFiles.length === 0) {
			alert("No control files were selected.");
			return;
		}
		if (experimentalFiles.length === 0) {
			alert("No experimental files were selected.");
			return;
		}
		if (pVal.length === 0) {
			alert("No p-value was entered.");
			return;
		}
		if (confInt.length === 0) {
			alert("No confidence interval was entered.");
			return;
		}

		var waitingWindow = document.createElement("div");
		waitingWindow.className = "waitingWindow";
		uiContainer.append(waitingWindow);
		$(waitingWindow).hide().fadeIn("slow");

		var waitingText = document.createElement("div");
		waitingText.className = "waitingText";
		waitingText.innerText = "Please wait... ";
		waitingWindow.append(waitingText);

		$.ajax({
			url: window.location.href + "runTestGeo/",
			type: "POST",
			contentType: "application/json",
			dataType: "json",
            headers: {
			    "X-CSRFToken" : csrftoken,
				"fileName" : fileName,
				"linkName" : linkName
            },
			data: JSON.stringify({
				controlFiles: controlFiles,
				experimentalFiles: experimentalFiles,
				pValue: pVal,
				confidenceInterval: confInt,
				dirName: folderName,
				test: "test1"
			})

            }).done(function(response){
                if (response.success) {
                    $(uiContainer).empty();
                    /*$(waitingWindow).remove();*/
                    generateGraph(uiContainer, response.data, folderName);
                }
                else {
                    alert("Something went wrong");
                }
        });


	});
	controlContainer.append(acceptControl);

	var cancelControl = document.createElement("input");
	cancelControl.type = "button";
	cancelControl.value = "Cancel";
	cancelControl.id = "IH-cancel";
	cancelControl.className = "cancelClass";
	controlContainer.append(cancelControl);

	uiContainer.append(controlContainer);

	cancelControl.addEventListener("click", function(e){
		$(uiContainer).fadeOut("slow");
		/*uiContainer.remove();*/
	})
};

function initPage() {
    //initialize list for user data
    var options = {
        valueNames: [ 'name', 'organism', 'description', 'link' ]
    };
    var geoDataList = new List('userData', options);

    var listSelect = document.getElementById("listSelect");
    listSelect.addEventListener("click", function(e) {

    	var csrftoken  = document.cookie.split("=");
        csrftoken = csrftoken[csrftoken.indexOf("csrftoken") + 1];
        var selectedRow, secondSelectedRow;
        if (e.target.className == "listItemLeft") {
            selectedRow = e.target.children[0];
            secondSelectedRow = e.target.children[3];
            fileName = selectedRow.children[0].innerText.split(" ").join("").split("\n").join("");
            linkName = secondSelectedRow.children[0].innerText.split(" ").join("").split("\n").join("");
        }
        else if ($(e.target).prop("nodeName").toLowerCase() === "p") {
        	selectedRow = e.target.parentElement.parentElement.parentElement.children[0];
            secondSelectedRow = e.target.parentElement.parentElement.children[3];
            fileName = selectedRow.children[0].innerText.split(" ").join("").split("\n").join("");
            linkName = secondSelectedRow.children[0].innerText.split(" ").join("").split("\n").join("");
		}
        else {
            selectedRow = e.target.parentElement.parentElement.children[0];
            secondSelectedRow = e.target.parentElement.parentElement.children[0].children[3]
            fileName = selectedRow.children[0].innerText.split(" ").join("").split("\n").join("");
            linkName = secondSelectedRow.children[0].innerText.split(" ").join("").split("\n").join("");
        }

    	$.ajax({
			url: "itemsInGeo/",
			type: "GET",
			contentType: "application/json",
			dataType: "json",
            headers: {
			    "X-CSRFToken" : csrftoken,
				"fileName": fileName,
				"linkName": linkName
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
