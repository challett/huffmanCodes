var i = 1;
function increment(){
  i += 1;
}

function addInput(){
  var text = document.createElement("INPUT");
  var number = document.createElement("INPUT");
  var row = document.createElement("div");

  row.setAttribute("class", "row")

  text.setAttribute("type", "text");
  text.setAttribute("class", "col s6")
  text.setAttribute("placeholder", "Symbol");

  number.setAttribute("type", "number");
  number.setAttribute("step", "0.0001");
  number.setAttribute("class", "col s5 offset-s1")
  number.setAttribute("placeholder", "P-Value");

  text.setAttribute("Name", "symbol_" + i);
  number.setAttribute("Name", "p_" + i);

  row.appendChild(text);
  row.appendChild(number);

  row.setAttribute("id", "row_id_" + i);

  increment();

  document.getElementById("pInputForm").appendChild(row);
}
