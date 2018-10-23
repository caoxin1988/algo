#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define N 6

int a[8] = {2, 5, 3, 0, 2, 3, 0, 3};
int counting[N] = {0,};

void counting_sort() {
    int b[8] = {0,};

    for (int j = 7; j >= 0; j--) {
        int value = a[j];
        int i = counting[value];
        b[i-1] = value;
        counting[value]--;
    }

    for (int i = 0; i < 8; i++) {
        printf("%d, ", b[i]);
    }
    printf("\n");
}

void get_counting() {

    for (int i =0; i < 8; i++) {
        int value = a[i];
        counting[value] += 1;
    }

    for (int i = 1; i < N; i++) {
        counting[i] += counting[i-1];
    }

}

int main() {

    get_counting();
    counting_sort();

    return 0;
}