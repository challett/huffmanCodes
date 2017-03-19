var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('codeResponse', function(data) {
    $("#results-container").html('');
    $("#average-length-container").html(data.averageCodeLength);
    $("#entropy-container").html(data.entropy);

    _.each(data.codes, function (item, key) {
      var resultRow = document.createElement("div");
      var resultName = document.createElement("div");
      var resultSymbol = document.createElement("div");

      resultRow.setAttribute("class", "row")
      resultName.setAttribute("class", "col s6");
      resultSymbol.setAttribute("class", "col s6");

      resultName.innerHTML = key;
      resultSymbol.innerHTML = item.code;

      resultRow.appendChild(resultName);
      resultRow.appendChild(resultSymbol);

      document.getElementById("results-container").appendChild(resultRow);
    })

    $('#result-modal').modal("open");
});

$(document).ready(function(){
   $('#result-modal').modal();
});

function onFormSubmit() {
  var returnArray = [],
      sum = 0;
  $("#mainform .row").each(function(i,item) {
    var pValue =  +$(item).children("input")[1].value,
        symbol = $(item).children("input")[0].value;
    if (pValue && symbol) {
      sum += pValue
      returnArray.push({
          symbol: symbol,
          p: pValue
      })
    }
  })

  if (sum === 1){
    socket.emit('calculateCodes', {data: returnArray});
    $("#p-sum-error").hide()
  }else {
    $("#p-sum-error").show()
  }
}

var i = 1;
function increment(){
  i += 1;
}

function decrement(){
  i -= 1;
}


function addInput(){
  var text = document.createElement("INPUT");
  var number = document.createElement("INPUT");
  var row = document.createElement("div");
  var button = document.createElement("button");

  row.setAttribute("class", "row")

  text.setAttribute("type", "text");
  text.setAttribute("class", "col s3")
  text.setAttribute("placeholder", "Symbol");
  text.setAttribute("Name", "symbol_" + i);
  text.setAttribute("id", "symbol_" + i);
  text.setAttribute("required", "required");

  number.setAttribute("type", "number");
  number.setAttribute("step", "any");
  number.setAttribute("class", "col s4 offset-s1")
  number.setAttribute("placeholder", "P-Value");
  number.setAttribute("Name", "p_" + i);
  number.setAttribute("id", "p_" + i);
  number.setAttribute("required", "required");
  number.setAttribute("max", "1");
  number.setAttribute("min", "0");

  button.setAttribute("class", "col s1 btn offset-s2");
  button.setAttribute("onClick", "removeInput(this)");
  button.innerHTML = "-"

  row.appendChild(text);
  row.appendChild(number);
  row.appendChild(button);

  row.setAttribute("id", "row_id_" + i);

  increment();

  document.getElementById("pInputForm").appendChild(row);
}

function removeInput(element){
  var row = element.parentElement;
  var rowParent = row.parentElement;
  rowParent.removeChild(row);
  decrement()
}
