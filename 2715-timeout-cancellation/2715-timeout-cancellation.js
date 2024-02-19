/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    let timeout = setTimeout(() => {
        fn(...args)
    }, t)

    return function() {
        clearTimeout(timeout)
    }

};