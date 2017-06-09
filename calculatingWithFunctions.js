// JavaScript Document
function zero(arg) {
  var num = 0;
  if (!arguments[0]) {
    return num;
  }
  return eval(num + arguments[0]);
}

function one(arg) {
  var num = 1;
  if (!arguments[0]) {
    return num;
  }
  return eval(num + arguments[0]);
}

function two() {var num = 0;
  var num = 2;
  if (!arguments[0]) {
    return num;
  }
  return eval(num + arguments[0]);
}
function three() {var num = 0;
  var num = 3;
  if (!arguments[0]) {
    return num;
  }
  return eval(num + arguments[0]);
}

function four() {var num = 0;
  var num = 4;
  if (!arguments[0]) {
    return num;
  }
  return eval(num + arguments[0]);
}

function five() {var num = 0;
  var num = 5;
  if (!arguments[0]) {
    return num;
  }
  return eval(num + arguments[0]);
}

function six() {var num = 0;
  var num = 6;
  if (!arguments[0]) {
    return num;
  }
  return eval(num + arguments[0]);
}

function seven() {var num = 0;
  var num = 7;
  if (!arguments[0]) {
    return num;
  }
  return eval(num + arguments[0]);
}

function eight() {var num = 0;
  var num = 8;
  if (!arguments[0]) {
    return num;
  }
  return eval(num + arguments[0]);
}

function nine() {var num = 0;
  var num = 9;
  if (!arguments[0]) {
    return num;
  }
  return eval(num + arguments[0]);
}

function plus() {
  return "+" + arguments[0];
}
function minus() {
  return "-" + arguments[0];
}
function times() {
  return "*" + arguments[0];
}
function dividedBy() {
  return "/" + arguments[0];
}
seven(times(five()));
four(plus(nine()));
eight(minus(three()));
six(dividedBy(two()));