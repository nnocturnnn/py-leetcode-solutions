var cancellable = function(fn, args, t) {
    let stop = false;
    fn(...args);

    const startTimer = () => {
        setTimeout(() => {
            if (stop) return;
            fn(...args);
            startTimer();
        }, t)
    }

   startTimer();

    const stopF = () => {
        stop = true;
    }

    return stopF;
};