#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define M 6
#define N 5

char a[M][N] = {"13572", "15734", "14269", "15384", "15721", "13852"};

void counting_sort(int n) {
    int counting[10] = {0,};
    char tmp[M][N] = {};
    
    for (int i = 0; i < M; i++) {
        char value = a[i][n] - 48;
        counting[value] += 1;
    }

    for (int i = 1; i < 10; i++) {
        counting[i] += counting[i-1];
    }

    for (int i = (M-1); i >= 0; i--) {
        char value = a[i][n] - 48;
        int j = counting[value];
        for (int k = 0; k < N; k++)
            tmp[j-1][k] = a[i][k];
        counting[value]--;
    }

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            // printf("%c", tmp[i][j]);
            a[i][j] = tmp[i][j];
        }
        // printf("\n");
    }

}

void base_sort() {
    for (int i = (N-1); i >= 0; i--) {
        counting_sort(i);
    }
}

int main() {

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            printf("%c", a[i][j]);
        }
        printf("\n");
    }
    printf("===================\n");

    base_sort();

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            printf("%c", a[i][j]);
        }
        printf("\n");
    }

    return 0;
}