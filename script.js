// GOAL: TO BE THE VERY BEST 

// If Else statements 
let hour = 'pizza';
const time = hour;

if (time < 12 ){
    console.log('Good Morning');
}

else if (time < 18 && time > 12){
    console.log('Good Afternoon');
}


else{
    console.log('Good Evening');
}

// Switch Statements


// Functions
// function = A section of reusable code.
//                    Declare code once, use it whenever you want.
//                    Call the function to execute that code.

function happyBirthday(username, age){
    console.log(`Happy birthday to you!`);
    console.log(`Happy birthday to you!`);
    console.log(`Happy birthday dear, ${username}`);
    console.log(`Happy birthday to you!`);
    console.log(`You are ${age} years old!`);
}

function add(x, y){
    return x + y;
}

function subtract(x, y){
    return x - y;
}

function multiply(x, y){
    return x * y;
}

function divide(x, y){
    return x / y;
}

function isEven(number){

    return number % 2 === 0 ? true : false;
}

function isValidEmail(email){

    return email.includes("@") ? true : false;
}

console.log(happyBirthday("BroCode", 25));
console.log(isValidEmail("Bro@fake.com"));




happyBirthday('Lamar', 23);

function favoriteAnimal(animal) {
    return animal + " is my favorite animal!"
}

console.log(favoriteAnimal('Goat'))




function foodPref (food, place){
    console.log(`I am feeling some ${food} from that ${place} spot up the road`)
}

foodPref('wings', 'Chinese');





const myArray = ["I", "love", "chocolate", "frogs"];
const madeAString = myArray.join(" ");
console.log(madeAString);
// the join() function takes an array, joins
// all the array items together into a single
// string, and returns this new string

const myNumber = Math.random();
// the random() function generates a random number between
// 0 and up to but not including 1, and returns that number



function greeting(){
    let hour = 4;
    const time = hour;

    if (time < 12 ){
        console.log('Good Morning');
    }

    else if (time < 18 && time > 12){
        console.log('Good Afternoon');
    }

    else{
        console.log('Good Evening');
    }
}

function specialDay(holiday,date){
    console.log(`${holiday} day will take place on ${date}!`);
}

specialDay('Earth', 'April 22nd 2024'); 

foodPref('Tuna Sub', 'Publix')

//  function inventory(){
//     let currentInventory = 3;
//      currentInventory --;
//      console.log(currentInventory);
//  }

 
let inventory = 4;

function subInventory(){
    inventory--;
    console.log(inventory);
 }

//  function addInventory(){
//     inventory++;
//     console.log(inventory);
//  }

 function addInventory(number){
   console.log(inventory + number);
 }
 
 addInventory(100);


