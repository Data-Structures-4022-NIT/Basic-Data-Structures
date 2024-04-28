function rotateArray(arr, k) {
  let n = arr.length;
  k = k % n;
  let rotatedArr = new Array(n);
  for (let i = 0; i < k; i++) {
    rotatedArr[i] = arr[n - k + i];
  }

  for (let i = k; i < n; i++) {
    rotatedArr[i] = arr[i - k];
  }

  return rotatedArr;
}

let array = [1, 2, 3, 4, 5];
let k = 2;
console.log(rotateArray(array, k));
