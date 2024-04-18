function mergeSortedArrays(array1, array2) {
  let counter1 = array1.length - 1;
  let counter2 = array2.length - 1;
  let counterMerge = array1.length + array2.length - 1;

  array1.length = counterMerge + 1;

  while (counter1 >= 0 && counter2 >= 0) {
    if (array1[counter1] > array2[counter2]) {
      array1[counterMerge] = array1[counter1];
      counter1--;
    } else {
      array1[counterMerge] = array2[counter2];
      counter2--;
    }
    counterMerge--;
  }

  while (counter2 >= 0) {
    array1[counterMerge] = array2[counter2];
    counter2--;
    counterMerge--;
  }

  return array1;
}

let array1 = [3, 6, 8, 11];
let array2 = [1, 4, 5, 7, 9, 10];
mergeSortedArrays(array1, array2);
console.log(array1);
