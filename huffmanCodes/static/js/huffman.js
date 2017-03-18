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

  number.setAttribute("type", "number");
  number.setAttribute("step", "0.0001");
  number.setAttribute("class", "col s4 offset-s1")
  number.setAttribute("placeholder", "P-Value");
  number.setAttribute("Name", "p_" + i);

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
