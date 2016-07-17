fun()
{
	document.getElementById("order").value = "You ordered a coffee ";
	var coffee = document.forms[0];
    var i;
    for (i = 0; i < coffee.length; i++) {

        if (coffee[i].checked) {
         	{% for spec,sent in picc %} 
         				{% if coffee[i].value == spec %}
									 var value = {{ sent|safe}};
									var ctx = $({{ "displaycharts" |safe}});
									var myChart = new Chart(ctx, {
									    type: 'doughnut',
									    data : {
									    labels: [
									        "Positive",
									        "Negative"
									    ],
									    datasets: [
									        {
									            data: [value, 10-value],
									            backgroundColor: [
									                "#5cd65c",
									                "#ff4d4d"
									            ],
									            hoverBackgroundColor: [
									                "#2eb82e",
									                "#ff1a1a"
									            ]
									        }]
									}
									});

         				{% endif %}

         	{% endfor %}   
        }
    }
	
}