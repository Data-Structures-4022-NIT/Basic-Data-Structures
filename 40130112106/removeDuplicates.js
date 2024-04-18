function removeDuplicates(array) {
  let lenOfArray = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] !== array[i - 1]) {
      lenOfArray++;
    }
  }
  return lenOfArray;
}

let array = [1, 2, 2, 3, 3, 3, 4, 5];
console.log(removeDuplicates(array));
