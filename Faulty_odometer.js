function faultyOdometer(n) {
    var start = 0;
    var count = 0;
    var start_local = 0;
    var count_local = 0;
    if (n >= 1000) {    // calculations
        n = String(n);
        var length = n.length;
        for (var num = 0; num < length - 2; num++) {
            if (Number(n[num]) >= 1 && Number(n[num]) <= 3) {
                start_local += Math.pow(10, length - 1) * Number(n[num]);     // brute force start
                count_local += start_local - Math.pow(9, length - 1) * Number(n[num]); // total occurence of 4's in n
                start += start_local;
                count += count_local;
                start_local = 0;
                count_local = 0;
            }
            else if (Number(n[num]) >= 5 && Number(n[num]) <= 9) {
                start_local += Math.pow(10, length - 1) * (Number(n[num]));
                count_local += start_local - Math.pow(9, length - 1) * (Number(n[num]) - 1);
                start += start_local;
                count += count_local;
                start_local = 0;
                count_local = 0;
            }
            length--;
        }
        n = Number(n);
    }
    for (var i = start; i < n; i++) { //brute force
        if (String(i).includes("4")) {
            count++;
        }
    }
    console.log(n - count);
    return n - count;
}
faultyOdometer(111111)