// ChartCreation

new Chart(document.getElementById("doughnut-chart"), {
    type: 'doughnut',
    data: {
      labels: [ 'USA',  'USSR_Russia', 'United_Kingdom', 'France', 'China', 'India', 'Pakistan', 'North_Korea'],
      datasets: [
        {
          label: "Number of Launches",
          backgroundColor: ["blue", "red","green","purple","yellow","orange", "pink","black"],
          data: [ 1031.0, 715.0, 45.0,   210.0,  45.0,   3.0,  2.0,    8.0 ]

        }


      ]
    },
    options: {
    
    	title: {
         titleFontSize: 30,
        display: true,
        text: "",
      }
    }
});


// function f_getDoughnut(){
// var defaultURL = "/doughnut";
// d3.json(defaultURL,function(x) {
// console.log(x);
// console.log(x.value);
// })}
