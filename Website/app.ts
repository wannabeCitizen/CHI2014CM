var width = 100;
var height = 25;
var x = d3.scale.linear().range([0, width - 2]);
var y = d3.scale.linear().range([height - 4, 0]);
var parseDate = d3.time.format("%b %d, %Y").parse;
var line = d3.svg.line()
    .interpolate("basis")
    .x(function (d) { return x(d.date); })
    .y(function (d) { return y(d.close); });

function sparkline(elemId, data) {
    x.domain(d3.extent(data, function (d) { return d.date; }));
    y.domain(d3.extent(data, function (d) { return d.close; }));

    var svg = d3.select(elemId)
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr('transform', 'translate(0, 2)');
    svg.append('path')
        .datum(data)
        .attr('class', 'sparkline')
        .attr('d', line);
    svg.append('circle')
        .attr('class', 'sparkcircle')
        .attr('cx', x(data[0].date))
        .attr('cy', y(data[0].close))
        .attr('r', 1.5);
}

function randomData() {
    var data = [];
    for (var i = 0; i < 15; i++) {
        data.push({ date: i, close: Math.random() });
    }
    return data;
}

function drawBar(html : d3.selection, data) {
        
    var s = data + ' percentile';
    html.textContent = s;
}

window.onload = () => {
    sparkline('#s1', randomData());
    sparkline('#s2', randomData());
    sparkline('#s3', randomData());

    var threeDims = [Math.round(Math.random() * 100), Math.round(Math.random() * 100), Math.round(Math.random() * 100)];

    var threeDimCaptions = ["attending sessions", "meeting people", "exploring the city"];

    d3.selectAll('.percentile ').data( threeDims ).each(function (d) { drawBar(this, d) });

    var maxVal = Math.max.apply(null, threeDims);
    var maxIndex = threeDims.indexOf(maxVal);

    var minVal = Math.min.apply(null, threeDims);
    var minIndex = threeDims.indexOf(minVal);


    var firststr = "Okay";
    if (maxVal > 50)
        firststr = "Good";
    if (maxVal > 80)
        firststr  = "Excellent";

    d3.select("#p4").html(firststr);
    d3.select("#a4").html( threeDimCaptions[ maxIndex] );

    var secondstr = "try to do a little more ";
    if (minVal < 50)
        secondstr = "improve your ";
    if (minVal < 20)
        secondstr = "spend a little more ";

    d3.select("#p5").html(secondstr);
    d3.select("#a5").html(threeDimCaptions[minIndex]);

};