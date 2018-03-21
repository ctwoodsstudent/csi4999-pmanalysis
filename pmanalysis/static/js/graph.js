function generateOverlay(conIntensity, expIntensity, sigProbes) {

	parent = document.body;
	var uiContainer = document.createElement("div");
	uiContainer.className = "uiGraphBody";
	parent.prepend(uiContainer);

	var headerContainer = document.createElement("div");
	headerContainer.className = "graphHeaderClass";
	uiContainer.append(headerContainer);

  var graphContainer = document.createElement("div");
  graphContainer.className = "graphClass";
  uiContainer.append(graphClass);

  var graphCanvas = document.createElement("canvas");
  graphCanvas.className = "canvasClass";
  graphCanvas.id = "pmanalysisChart";
  graphContainer.append(graphCanvas);

  generateGraph(conIntensity, expIntensity, sigProbes);
}

function generateGraph(conIntensity, expIntensity, sigProbes) {

  var jQueryScript = document.createElement('script');
  jQueryScript.setAttribute('src','https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js');
  document.head.appendChild(jQueryScript);

  var ctx = document.getElementById("pmanalysisChart").getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Red", "Blue"],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});
}
