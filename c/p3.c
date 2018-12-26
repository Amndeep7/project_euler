/*
 * https://projecteuler.net/problem=3
 * Largest prime factor
 */

#include <math.h>
#include <stdbool.h>
#include <stdio.h>

long max_prime(long num) {
	int root = (int)(sqrt(num));
	printf("Creating sieve of size %d\n", root);
	root++; // have to include root as a possible index
	bool sieve[root];
	for(int i = 0; i < root; i++) {
		sieve[i] = true;
	}

	printf("Processing sieve\n");
	sieve[0] = false;
	sieve[1] = false;
	for(int i = 2*2; i < root; i += 2) {
		sieve[i] = false;
	}
	printf("Killed 2's\n");
	for(int i = 6; i < root; i+=6) {
		if(sieve[i-1] == true) {
			for(int j = (i-1) * 2; j < root; j += (i-1)) {
				sieve[j] = false;
			}
		}
		if(i+1 < root && sieve[i+1] == true) {
			for(int j = (i+1) * 2; j < root; j += (i+1)) {
				sieve[j] = false;
			}
		}
	}

	printf("Identifying maximum\n");
	long ret = root - 1;
	while(ret >= 0) {
		if(sieve[ret] == true && num % ret == 0) {
			return ret;
		}
		ret -= 1;
	}
	return num;
}

int main() {
	printf("Hello\n");
	printf("%d\n", max_prime(600851475143));
	return 0;
}
