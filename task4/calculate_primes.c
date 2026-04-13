#include "calculate_primes.h"

void calculate_primes(int primes[], int n) {
    int k, l;

    /* нам известно, что числа 0 и 1 не простые */
    primes[0] = 0;
    primes[1] = 0;

    /* осуществляем поиск простых чисел */
    for (k = 2; k <= n; k++) {
        primes[k] = 1; /* делаем все значения единицами */
    }
    /* решето Эратосфена */
    for (k=2; k*k<=n; k++) {
        if (primes[k]) {
            for (l = k * k; l <= n; l += k) {
                primes[l] = 0;
            }
        }
        
    }

}