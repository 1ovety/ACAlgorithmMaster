/**
 * 476. Number Complement
 * The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

    For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
    Given an integer num, return its complement.
 * Example 1:

    Input: num = 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
    Example 2:

    Input: num = 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
    
    Constraints:
    1 <= num < 231
 */

/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function (num) {
    let binary = Array.from(num.toString(2));
    // console.log(binary);
    for (let i = 0; i < binary.length; i++){
        if (binary[i] == 0) {
            binary[i] = 1;
        } else {
            binary[i] = 0;
        }
    }
    
    return parseInt(binary.join(''), 2);
    
};

var num = 20161211;
console.log(findComplement(num));