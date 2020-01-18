// from data.js
var tableData = data;

// select table body
tbody = d3.select("tbody")

// add data to html table
function displayData(data){ 
    tbody.html()
    data.forEach(function(sighting){
    new_tr = tbody.append("tr")
    Object.entries(sighting).forEach(function([key, value]){
        new_td = new_tr.append("td").text(value)	
    })
})}

displayData(tableData)