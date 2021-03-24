// 1. Ways to print
// TODO:Format add code and Topic make this as python learning
//   alert("this is alert we do not use this more");
//   document.write("right"); //we should avoid this
//   console.log("hello world");
//   we should  end any statement with ;(this should be kept but javascript forgives it)

// 2. javascript console API

// console.log("hello world", "we can log multiple stuff", 4 + 5);
// console.warn("this is a warning");
// console.error("this is a error");
// console.log(this) // this is refered has to the Element

// 3. ways to write comments

// comments are something that computer should ignore this is for notes
// this is a single line comment
/*this is a multi 
line comment*/

// 4. Variables-containers to store values

// making variables
// we can use both "var" and "let" (recommended) keywords (reserved words in javascript)

// making constants
// const bc = 2; // this is a constant (cannot be changed)

// 5. DataTypes

// These are a number literals (these contain all float,integers)
var aNumber = 1;
anotherNumber = 2;
console.log(aNumber + anotherNumber);

// These are string literals (set of characters)
var aStr = "this is a string";
var anotherStr = "this is another string with double quotes";
console.log(aStr, anotherStr);
// These are boolean literals (true and false)

var aBoolean = true;
var anotherBoolean = false;
console.log(aBoolean, anotherBoolean);

// This is undefined(not defined) datatype
// Every variable's default value is undefined

var aUndefined = undefined;
console.log(aUndefined);

// This is null(nothing) datatype
// null is different from undefined because
// We are telling there is nothing in variable

var aNull = null;
console.log(aNull);

// This is a object
// Object has key and values

var person = {
  name: "madhav",
  age: 8,
};

console.log(person); // to show total object
console.log(person.age); // for a particular value of a key
console.log(person[0]); //to show value of key by index(in javascript counting starts from 0)

// These are arrays
// Arrays are collection of values
var aArray = [1, 2, 3, 4, 5];
var anotherArray = [1, 2, 3, true, "hello"]; // arrays can be written in different datatypes
console.log(aArray, anotherArray);

/* there are two types of DataTypes:
1.primitive data types(inbuilt):undefined, null, number, string, boolean, symbol()
2.reference data types(made by us):arrays, objects
*/

// 6. Operators

// Arithmetic operators (for operations)

var one = 1645;
var two = 645;
console.log(one + two);
console.log(one - two);
console.log(one * two);
console.log(one ** two); // for exponents
console.log(one / two);

// Assignment operators(for assigning values)

var one = two;
console.log((one += 2));
console.log((one -= 3));
console.log((one *= 5));
console.log((one /= 4));

// Comparison operators

console.log(1 == 2);
console.log(1 > 2);
console.log(1 < 2);
console.log(1 >= 2);
console.log(1 <= 2);

// Logical operators (and,or,not)

// and (this only accepts when both are true)

console.log(true && true);
console.log(true && false);
console.log(false && true);
console.log(false && false);

// or (this accepts when anyone is true)

console.log(true || true);
console.log(true || false);
console.log(false || true);
console.log(false || false);

// not (reverses the output)

console.log(!true);
console.log(!false);

/*operator is between values
operands are the values*/

// 7. functions
// These are certain statements executed at once

function add(a, b) {
  q = a + b;
  return q;
}

// We should call function to execute

// One way to calling function
c = add(4, 6);
console.log(c);

// Another way of calling function
// This is function inside function

console.log(add(1, 2));

// Functions have name, parameters (variables that only can be used inside of function), statements

/*function name(parameters) { (for going inside function)
    statements for execution
}*/

// Functions use DRY=do not repeat yourself

// Google console represents the Data Types in different colors

// 8.conditionals(if,else)

var age = 1;

// if statement

if (age > 10) {
  console.log("you are not a kid");
}

// if-else statement

if (age > 10) {
  console.log("you are not a kid");
} else {
  console.log("you are a kid");
}

// if-else ladder

if (age > 1) {
  console.log("you are not a kid");
} else if (age > 5) {
  console.log("you are a kid");
} else {
  console.log("you are good kid");
}

// when condition satisfies the program comes out of it

// 9.repetition control(loops)

var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];

// for loop

for (var i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

// foreach loop
// better for iteration of collections

arr.forEach(function (element) {
  console.log(element);
});

let j = 0; //recommended ways to declare variables

// while loop
// this runs only if condition is true

while (j < arr.length) {
  console.log(arr[j]);
  j++;
}

// do while loop
// this runs at least one time before checking condition
do {
  console.log(arr[j]);
  j++;
} while (j < arr.length);

// break and continue

for (var i = 0; i < arr.length; i++) {
  if (i == 2) {
    // break; //go away from this loop
    // continue; //skip this iteration
  }
  console.log(arr[i]);
}

// 10.methods

// Array methods

let newArr = ["fan", "man", 34, 6.7, null, true];

console.log(newArr.length);
console.log(newArr.pop());
console.log(newArr.push("me"));
console.log(newArr.shift());
console.log(newArr.unshift("mine"));
console.log(newArr.toString());
console.log(newArr.sort()); //alphabet sort

// String methods

let myString = "madhav is a medium boy";

console.log(myString.length);
console.log(myString.indexOf("madhav"));
console.log(myString.lastIndexOf("madhav"));
console.log(myString.slice(0, 3));
console.log(myString.replace("madhav", "madhav is")); //only changes first occurrence

// 11.Date and time

let myDate = new Date();
// new is for making new date
console.log(myDate);
console.log(myDate.getTime);
console.log(myDate.getDate);
console.log(myDate.getDay);
console.log(myDate.getFullYear);
console.log(myDate.getMilliseconds);

// 12.dom manipulation
// DOM-document(webpage,html) object model
// we can change our page by javascript
let w = document.getElementById("click");
console.log(w);

let x = document.getElementsByClassName("container");
console.log(x);
// x[0].style.background = "red";

x[0].classList.add("bg-primary");

x[0].classList.add("text-success");

// classList.remove -->removes class form classlist

console.log(x.innerText);
console.log(x.innerHTML);
console.log(x[0].innerText);
console.log(x[0].innerHTML);

let tn = document.getElementsByTagName("button");
console.log(tn);

let createdElement = document.createElement("p");
createdElement.innerText = "this is js para";
tn[0].appendChild(createdElement);
let createdElement2 = document.createElement("b");
createdElement2.innerText = "this is bold js para";
tn[0].replaceChild(createdElement2, createdElement);
// removeChild(element); --> removes element

let y = document.querySelector(".container");
console.log(y);

let y1 = document.querySelectorAll(".container");
console.log(y1);

// 13.Events
// event are stuff that happens like clicking button

function clicked() {
  console.log("The button was clicked");
}
window.onload = function () {
  console.log("The document was loaded");
};

firstContainer.addEventListener("click", function () {
  document.querySelectorAll(".container")[1].innerHTML =
    "<b> We have clicked</b>";
  console.log("Clicked on Container");
});

firstContainer.addEventListener("mouseover", function () {
  console.log("Mouse on Container");
});

firstContainer.addEventListener("mouseout", function () {
  console.log("Mouse out of Container");
});

let prevHTML = document.querySelectorAll(".container")[1].innerHTML;
firstContainer.addEventListener("mouseup", function () {
  document.querySelectorAll(".container")[1].innerHTML = prevHTML;
  console.log("Mouse up when clicked on Container");
});

firstContainer.addEventListener("mousedown", function () {
  document.querySelectorAll(".container")[1].innerHTML =
    "<b> We have clicked</b>";
  console.log("Mouse down when clicked on Container");
});

// 14.Arrow Functions

summ = (a, b) => {
  return a + b;
};

logging = () => {
  document.querySelectorAll(".container")[1].innerHTML =
    "<b> Set interval fired</b>";
  console.log("I am your log");
};
// 15.SetTimeout and setInterval

// clr = setTimeout(logging, 5000);
// clr = setInterval(logging, 2000);
// use clearInterval(clr)/clearTimeout(clr) to cancel setInterval/setTimeout

// setTimeout-for doing something after sometime
// setInterval-for doing something repeatedly with gap

// 16.JavaScript localStorage

localStorage.setItem("name", "pranay");
localStorage.getItem("name");
localStorage.removeItem("name");
localStorage.clear();

// 17.Json
// this is used for transporting data easily
obj = { name: "pranay", length: 1, a: { this: 'tha"t' } };
jso = JSON.stringify(obj);
console.log(typeof jso);
console.log(jso);
parsed = JSON.parse(`{"name":"pranay","length":1,"a":{"this":"that"}}`);
console.log(parsed);

// 18.Template literals - Backticks
a = 34;
console.log(`this is my ${a}`);

// Documentation:https://www.w3schools.com/jsref/default.asp

