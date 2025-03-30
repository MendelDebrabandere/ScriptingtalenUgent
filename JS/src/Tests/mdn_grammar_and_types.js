
let foo = {
  "jema" : 3,
  "bar" : "blblbl",
  "fortnite" : "battlepass"
};

const { bar } = foo; // gets the value connected to key 'bar' in foo

console.log(bar);

// let x;
// console.log(x); // logs "undefined"


// A variable may belong to one of the following scopes:
//
//   Global scope: The default scope for all code running in script mode.
//   Module scope: The scope for code running in module mode.
//   Function scope: The scope created with a function.
//
// In addition, variables declared with let or const can belong to an additional scope:
//
//   Block scope: The scope created with a pair of curly braces (a block).

// if (Math.random() > 0.5) {
//   const y = 5;
// }
// console.log(y); // ReferenceError: y is not defined

// However, variables created with var are not block-scoped, but only local to the function (or global scope) that the block resides within.
if (1) {
  var y = 5;
}
console.log(y); // y is 5

// var-declared variables are hoisted, meaning you can refer to the variable
// anywhere in its scope, even if its declaration isn't reached yet.
// You can see var declarations as being "lifted" to the top of its function or global scope.
// However, if you access a variable before it's declared, the value is always undefined,
// because only its declaration and default initialization (with undefined) is hoisted,
// but not its value assignment.
