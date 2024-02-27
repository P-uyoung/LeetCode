/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var start = 0,
        temp = '',
        result = ''
    for (let i = 0; i < s.length; i ++) {
        let index = temp.indexOf(s[i])
        if (index !== -1) {
            start = start + index + 1
        }
        temp = s.substring(start, i + 1)
        if (result.length < temp.length) {
            result = temp
        }
    }
    return result.length
};