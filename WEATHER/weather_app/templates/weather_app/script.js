/**
 * Created by DELL on 11-06-2018.
 */
// Our labels along the x-axis
var years = [1,2,3,4,5];
// For drawing the lines
var content =[1,2,3,4,5];

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: years,
    datasets: [

        {
            data : content,
            label: "Temperature",
            borderColor: "#3e95cd",
            fill: false
        }
    ]
  }
});
