//  The For Loop
for (let i=5; i<11;i++) {
    console.log(i);
  }

//  Looping in Reverse
for (let counter = 3; counter >= 0; counter--){
    console.log(counter);
  }

//  Looping through Arrays
const vacationSpots = ['Bali', 'Paris', 'Tulum'];
for (let i=0; i<vacationSpots.length; i++) {
  console.log('I would love to visit '+vacationSpots[i]);
}

//  Nested Loops
const bobsFollowers = ['1', '2', '3', '4']
const tinasFollowers = ['5', '4', '3'];
const mutualFollowers = [];

for (let i = 0; i < bobsFollowers.length; i++) {
  for (let j = 0; j < tinasFollowers.length; j++) {
    if (bobsFollowers[i] === tinasFollowers[j]) {
      mutualFollowers.push(bobsFollowers[i]);
      console.log(mutualFollowers);
    }
  }
}

//  The While Loop
const cards = ['diamond', 'spade', 'heart', 'club'];
let currentCard;

while (currentCard != 'spade'){
  currentCard = cards[Math.floor(Math.random() * 4)];
  console.log(currentCard);
}

//  Do...While Statements
let cupsOfSugarNeeded = Math.floor(Math.random() * 10);
let cupsAdded = 0;

do {
  console.log(cupsAdded);
  cupsAdded++
} while (cupsAdded < cupsOfSugarNeeded);

//  The break Keyword
const rapperArray = ["Lil' Kim", "Jay-Z", "Notorious B.I.G.", "Tupac"];

// Write your code below
for (let i=0; i < rapperArray.length; i++) {
  if (rapperArray[i] === 'Notorious B.I.G.') {
    console.log(rapperArray[i]);
    break;
  }
  console.log(rapperArray[i]);
}
console.log("And if you don't know, now you know.");