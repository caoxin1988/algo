#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define N 10
int a[N] = {1, 6, 3, 8, 15, 6, 7, 3, 12, 10};

void quick_sort(int *a, int p, int q) {

    if (p >= q) {
        return;
    }

    int j = p;
    int povit = a[q];

    for (int i = p; i < q+1; i++) {
        if (a[i] < povit) {
            int tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;

            j++;
        }
    }

    int tmp = a[j];
    a[j] = a[q];
    a[q] = tmp;

    quick_sort(a, p, j-1);
    quick_sort(a, j+1, q);
}

int main() {
    quick_sort(a, 0, N-1);

    for (int i = 0; i < N; i++)
        printf("%d, ", a[i]);
    printf("\n");
    return 0;
}