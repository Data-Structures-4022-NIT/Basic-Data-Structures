function findMissingNumber(array) {
  let n = array.length;
  let sum = (n * (n + 1)) / 2;
  let sumOfElementArray = 0;
  for (let i = 0; i < array.length; i++) {
    sumOfElementArray += array[i];
  }
  let missingNumber = sum - sumOfElementArray;
  return missingNumber;
}

let array = [0, 1, 2, 3, 5];
console.log(findMissingNumber(array));
