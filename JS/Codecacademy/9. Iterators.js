//      The .forEach() Method
    const fruits = ['mango', 'papaya', 'pineapple', 'apple'];

    fruits.forEach(fruitsItem => 
    console.log('I want to eat a ' + fruitsItem));

//      The .map() Method (returns a new array)
    const animals = ['Hen', 'elephant', 'llama', 'leopard', 'ostrich', 'Whale', 'octopus', 'rabbit', 'lion', 'dog'];

    const secretMessage = animals.map(item => {
    return item.substr(0,1);
    })
    console.log(secretMessage.join(''));

    const bigNumbers = [100, 200, 300, 400, 500];
    const smallNumbers = bigNumbers.map(item => {
    return item/100;
    });
    console.log(bigNumbers);
    console.log(smallNumbers);

//      The .filter() Method (returns a new array)
    const randomNumbers = [375, 200, 3.14, 7, 13, 852];
    const smallNumbers = randomNumbers.filter(item => { return item < 250})
    console.log(smallNumbers);

    const favoriteWords = ['nostalgia', 'hyperbole', 'fervent', 'esoteric', 'serene'];
    const longFavoriteWords = favoriteWords.filter(item => {return item.length > 7})
    console.log(longFavoriteWords);

//      The .findIndex() Method
    const animals = ['hippo', 'tiger', 'lion', 'seal', 'cheetah', 'monkey', 'salamander', 'elephant'];

    const foundAnimal = animals.findIndex(item => {
    return item === 'elephant';
    });
    console.log(animals[foundAnimal]);

const startsWithS = animals.findIndex(item => {
    //return item[0] === 's';
    return item.charAt(0) === 's';
    });
    console.log(animals[startsWithS]);

//      The .reduce() Method
    const newNumbers = [1, 3, 5, 7];

    const newSum = newNumbers.reduce(function(accumulator, currentValue){
    console.log('The value of accumulator: ', accumulator);
    console.log('The value of currentValue: ', currentValue);
    return accumulator + currentValue
    }, 10);
    console.log(newSum);

//      Iterator Documentation
//      link = 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#Iteration_methods'
    const words = ['unique', 'uncanny', 'pique', 'oxymoron', 'guise'];

    console.log(words.some(word => {
    return word.length < 6;
    }));

    const interestingWords = words.filter(item => {
    return item.length > 5;
    })

    console.log(interestingWords.every((word) => { 
    return word.length > 5;
    } ));

//      Choose the Right Iterator
    const cities = ['Orlando', 'Dubai', 'Edinburgh', 'Chennai', 'Accra', 'Denver', 'Eskisehir', 'Medellin', 'Yokohama'];

    const nums = [1, 50, 75, 200, 350, 525, 1000];

    //  Choose a method that will return undefined
    cities.forEach(city => console.log('Have you visited ' + city + '?'));

    // Choose a method that will return a new array
    const longCities = cities.filter(city => city.length > 7);

    // Choose a method that will return a single value
    const word = cities.reduce((acc, currVal) => {
        return acc + currVal[0]
    }, "C");

    console.log(word)   //  CODECADEMY

    // Choose a method that will return a new array
    const smallerNums = nums.map(num => num - 5);

    // Choose a method that will return a boolean value
    nums.some(num => num < 0);