/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let fizzBuzz = new Array();
       for (let j = 1; j <= n; j++ ){
           if (j % 3 == 0 && j % 5 == 0)
               fizzBuzz[j-1] = "FizzBuzz";
           else if (j%3 == 0 )
               fizzBuzz[j-1] = "Fizz";
           else if (j%5 == 0)
               fizzBuzz[j-1] = "Buzz";
           else
               fizzBuzz[j-1] = j.toString();
       }
       return fizzBuzz;
};