var createCounter = function(init) {

    let ori = init

    return {
        increment: () => {
            ori += 1
            return ori
        },
        decrement: () => {
            ori -= 1
            return ori
        },
        reset: () => {
            ori = init
            return ori
        }
    }
};