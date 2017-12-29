var dataAggr = [['2009-10-01',0.09995788162779434],['2010-10-01',0.677771482164246],['2011-04-01',0.5419786950363602],['2011-10-01',0.429761746592623],['2012-04-01',0.5553930883332024],['2012-10-01',0.8338521353061876],['2013-04-01',0.8917532592567559],['2013-10-01',0.7663047304256949],['2014-04-01',0.636633751586632],['2014-10-01',0.587346447183409],['2015-04-01',0.45338037580817414],['2015-10-01',0.3331507300415433],['2016-04-01',0.4055031658222447],]




window.onload = function() {
	main()
}

function main() {
	for(var i = 0; i < dataAggr.length; i++){
		console.log(dataAggr[i]);
	}
}

function graph() {
	var formatDate = d3.time.format("%d-%b-%y");


	var x = d3.time.scale()
	    .range([0, 400]);

	var y = d3.scale.linear()
    	.range([400, 0]);


	var line = d3.svg.line()
	    .x(function(dataAggr) { return x(d[0]); })
	    .y(function(dataAggr) { return y(d[1]); });

	var firstSvgContainer = d3.select("#graph").append("svg")
							.attr("width", 1000)
							.attr("height", 1000)
							.attr("class", "svgTimeline");

	firstSvgContainer.append("g")
						  .attr("class", "axis")
						  .attr("transform", 'translate(0, 10)') //Moves up and down
						  .call(x);

	firstSvgContainer.append("g")
						  .attr("class", "axis")
						  .attr("transform", 'translate(0, 10)') //Moves up and down
						  .call(y);





}