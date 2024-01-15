/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {

    const arrLen = arr.length;
    if (arrLen === 0) return [];

    let newArr = [];

    let count = 0;

    while (count < arrLen){
        newArr.push(arr.slice(count,count + size));
        count += size
    }

    return newArr
};
