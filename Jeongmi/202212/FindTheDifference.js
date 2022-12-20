/**
 * 389. Find the Difference
 * You are given two strings s and t.

    String t is generated by random shuffling string s and then add one more letter at a random position.

    Return the letter that was added to t.

    

    Example 1:

    Input: s = "abcd", t = "abcde"
    Output: "e"
    Explanation: 'e' is the letter that was added.
    Example 2:

    Input: s = "", t = "y"
    Output: "y"
    

    Constraints:

    0 <= s.length <= 1000
    t.length == s.length + 1
    s and t consist of lowercase English letters.
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {

    // if the s length is less than 0 return t
    if (s.length <= 0) {
        return t;
    } else {
        // Sort s and t 
        let orderedS = s.split('').sort().join('');
        let orderedT = t.split('').sort().join('');

        var length = orderedT.length;

        // looping through all the elements in the t and s string
        for (let i = 0; i < length; i++){
            // if the orderedS string is less than 0 then return the orderedT[0]
            if (orderedS.length <= 0) {
                return orderedT[0];
            }
            
            // if the character is equal remove the character and keep searching differences
            if (orderedT[0] == orderedS[0]) {
                orderedS = orderedS.substring(1);
                orderedT = orderedT.substring(1);
            } else {
                return orderedT[0];
            }
             
   
        }
     
    }

    
};

var s = "abcd";
var t = "abcde";
console.log(findTheDifference(s, t));