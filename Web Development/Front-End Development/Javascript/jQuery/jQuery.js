// this keyword: This is referred to the selector's html
$("p").click(function () {
  console.log(this);
});

// Topic: Events in jQuery
// SubTopic: click Event (A action by user in our website)

// To click on element
$("p").click();

// To run a function on click
$("p").click(function () {
  console.log("Clicked")
});

// To run a function on  double click
$("p").dblclick(function () {
  console.log("Double Clicked")
});

// SubTopic: Hover
// To run functions on  hover
$("p").hover(
  function () {
    console.log("Came")
  },
  function () {
    console.log("Gone")
  }
);

// SubTopic: on method
$("div").on({
  click: function () {
    console.log("Clicked")
  },
  dblclick: function () {
    console.log("Double Clicked")
  },
});

// Topic: Animations
$("div").hide(2000, function () {
  console.log("Hiding")
});

$("div").show(5005, function () {
  console.log("Showing")
});

$("div").fadeIn(2008);
$("div").fadeOut(2008);
$("div").fadeToggle(2008);
$("div").fadeTo(2008);

// SubTopic: Slide methods
$("div").slideUp(4675, function () {
  console.log("Slide")
});
$("div").slideDown(4675);
$("div").slideToggle(4675);

// SubTopic: Animate function
$("div").animate(
  {
    opacity: 0.3,
    height: "150px",
    width: "350px",
  },
  "fast"
);

$("p").animate({ opacity: 0.3 }, 6785);
$("p").animate({ opacity: 0.9 }, 6785);
$("p").animate({ width: "350px" }, 6785);

// Topic: DOM Manipulation
$("div").val("content");
$("div").html("content");
$("div").html("content");
$("div").html("content");
$("div").val("content");
$("div").empty();
$("div").empty();
$("div").text("content");
$("div").remove();
$("div").addClass("classname");
$("div").removeClass("classname");

// Topic: CSS
$("div").css("background", "red");

// SubTopic: To get value of property
$("h1").css("background");

// Topic: AJAX

//SubTopic: Get
$.get("https://www.google.com/", function (data, status) {
  alert(data);
  alert(status);
});

//SubTopic: Post
$.post(
  "https://www.google.com/",
  // Content to post,
  function (data, status) {
    alert(status);
    alert(data);
  }
);

// It is good to run jquery when every thing is loaded in document.
// To do this put jQuery in this function.
$(document).ready(function () {
  Here;
});
