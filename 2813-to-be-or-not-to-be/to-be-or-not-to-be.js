/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: (par) => {
            if (par === val) {
                return true;
            } else {
                throw new Error("Not Equal");
            }
        },
        notToBe: (par) => {
            if (par !== val) {
                return true;
            } else {
                throw new Error("Equal");
            }
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */