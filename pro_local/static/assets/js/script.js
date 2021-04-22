function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function killCookie(cname, exdays) {
  var d = new Date();
  d.setTime(d.getTime() - (exdays*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + ";" + expires + ";path=/";
}

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

//COOKIE FORMAT: PLCART-SNAME-PNAME
//the following 

function cartCookies(){
//find the value of the given cookies 
var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function createShopNode(image, name, store, price, distance){
//the outer div
var box = document.createElement("div");
//The main container for content
var container = document.createElement("div");
container.setAttribute("class", "container");
box.appendChild(container);
//the dashed line at the end of the content
var dashedLine = document.createElement("hr");
dashedLine.setAttribute("class", "dashed");
box.appendChild(dashedLine);
//the row, used for spacing
var row = document.createElement("div");
row.setAttribute("class", "row");
container.appendChild(row);
//the column and image stored
var imgCol = document.createElement("div");
imgCol.setAttribute("class", "col-md-4");
row.appendChild(imgCol);
var proImg = document.createElement("img");
proImg.setAttribute("src", image);
proImg.setAttribute("width", "100");
proImg.setAttribute("height", "100");
imgCol.appendChild(proImg);
//Product name and store
var infoCol = document.createElement("div");
infoCol.setAttribute("class", "col-md-4");
row.appendChild(infoCol);
//product name structure
var proLink = document.createElement("a");
infoCol.appendChild(proLink);
var proName = document.createElement("strong");
proName.setAttribute("style", "color: rgb(73,11,61);");
var proNameText = document.createTextNode(name);
proName.appendChild(proNameText);
proLink.appendChild(proName);
//store name structure
var stoLink = document.createElement("a");
infoCol.appendChild(stoLink);
var stoName = document.createElement("p");
stoName.setAttribute("style", "color: rgb(125, 130, 133);");
var stoNameText = document.createTextNode(store);
stoName.appendChild(stoNameText);
stoLink.appendChild(stoName);
//Product cost and distance
var costCol = document.createElement("div");
infoCol.setAttribute("class", "col-md-4");
row.appendChild(costCol);
//product cost structure
var monLink = document.createElement("a");
costCol.appendChild(monLink);
var monName = document.createElement("strong");
monName.setAttribute("style", "color: rgb(73,11,61);");
var monNameText = document.createTextNode("$"+price);
monName.appendChild(monNameText);
monLink.appendChild(monName);
//store distance structure
var dstLink = document.createElement("a");
costCol.appendChild(dstLink);
var dstName = document.createElement("p");
dstName.setAttribute("style", "color: rgb(125, 130, 133);");
var dstNameText = document.createTextNode(distance+" Km");
dstName.appendChild(dstNameText);
dstLink.appendChild(dstName);
//aligned ADD TO CART BUTTON
var addToCart = document.createElement("div");
addToCart.setAttribute("class", "aligned");
costCol.appendChild(addToCart);
var addToCartBTN = document.createElement("button");
addToCartBTN.setAttribute("style", "background: #bd1e51;");
addToCartBTN.setAttribute("class", "btn btn-primary");
addToCartBTN.setAttribute("type", "button");
var addToCartBTNTXT = document.createTextNode("Add to cart");
addToCartBTN.appendChild(addToCartBTNTXT);
addToCart.appendChild(addToCartBTN);


}