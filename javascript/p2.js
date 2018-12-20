/*
 * https://projecteuler.net/problem=2
 * Even Fibonacci numbers
 */

const attempt1 = (upper_value_bound) => {
	const fib = [1, 2];
	for (let i = 2; fib[i-1]+fib[i-2] <= upper_value_bound; i++) {
		fib.push(fib[i-1]+fib[i-2]);
	}
	return fib.reduce((acc, cur) => cur % 2 === 0 ? acc + cur : acc, 0);
}

const attempt2 = (upper_value_bound) => {
	let sum = 0;
	let a = 1;
	let b = 2;
	while (b <= upper_value_bound) {
		if (b % 2 === 0) {
			sum += b;
		}
		const temp = b;
		b = a + b;
		a = temp;
	}
	return sum;
}

console.log(attempt2(4000000));
