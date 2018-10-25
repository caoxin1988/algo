#include <stdio.h>
#include <stdlib.h>

#define N 10

int a[N] = {7, 6, 3, 8, 15, 6, 7, 3, 12, 10};

void bubble_sort() {

    for(int i = 0; i < N; i++) {
        for (int j = 0; j < (N-i-1); j++) {
            if (a[j] > a[j+1]) {
                int tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
            }
        }
    }

    printf("new array: \n");
    printf("    ");
    for (int i = 0; i < N; i++)
        printf("%d ", a[i]);
    printf("\n");
}

// int a[N] = {7, 6, 3, 8, 15, 6, 7, 3, 12, 10};
void insert_sort() {

    for(int i = 1; i < N; i++) {
        int tmp = a[i];
        printf("tmp = %d\n", tmp);
        int j = i - 1;
        for (j = i-1; j >= 0; j--) {
            printf("a[i] = %d, a[j]=%d\n", a[i], a[j]);
            if (tmp < a[j]) {
                a[j+1] = a[j];
            } else {
                break;
            }
        }

        a[j + 1] = tmp;
    }

    printf("new array: \n");
    printf("    ");
    for (int i = 0; i < N; i++)
        printf("%d ", a[i]);
    printf("\n");
}

// int a[N] = {1, 6, 3, 8, 15, 6, 7, 3, 12, 10};
void select_sort() {

    for(int i = 0; i < N; i++) {
        int min = a[i];
        int t = i;
        for (int j = (i+1); j < N; j++) {
            if (a[j] < min) {
                min = a[j];
                t = j;
            }
        }

        if (t != i) {
            a[t] = a[i];
            a[i] = min;
        }
    }

    printf("new array: \n");
    printf("    ");
    for (int i = 0; i < N; i++)
        printf("%d ", a[i]);
    printf("\n");
}

int main() {

    // bubble_sort();
    insert_sort();

    return 0;
}