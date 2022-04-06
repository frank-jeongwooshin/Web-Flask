// JS 문법
// 변수 
let number = 3;
let name = "Frank";
let realNum = 3.14;
const NUM = 3;
const NAME = "FRANK";
const PIE = 3.141592;

// alert vs consol
alert(NAME);
console.log(realNum);

// input
let client = prompt("What is Your Name ?");
alert(`Hello, ${client}`);

// function
function add(num1, num2)
{
    return num1 + num2;
}

let result = add(3, 6);
console.log(result);

function divide(num1, num2)
{
    if (num2 == 0)
    {
        alert("can't divide by 0");
        return "Try Again";
    }
    return num1 / num2;
}

result = divide(3,0);
console.log(result);