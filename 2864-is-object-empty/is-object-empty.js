/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if (JSON.stringify(obj) !== '{}' && JSON.stringify(obj) !== '[]') {
        return false
    } else {
        return true
    }
};