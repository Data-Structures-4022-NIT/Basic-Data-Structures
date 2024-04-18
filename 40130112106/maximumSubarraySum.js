function maximumSubarraySum(array) {
  let n = array.length;
  let max = array[0];
  for (let i = 0; i < n; i++) {
    let s = array[i];
    if (s >= max) {
      max = s;
    }
    let j = i + 1;
    while (j < n) {
      s += array[j];
      if (s >= max) {
        max = s;
      }
      j++;
    }
  }
  return max;
}

let array = [1, 5, -1, -50, 3, 4, 7, -5];
console.log(maximumSubarraySum(array));
