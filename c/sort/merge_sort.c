#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define N 10
int a[N] = {1, 6, 3, 8, 15, 6, 7, 3, 12, 10};

void merge(int *a, int p, int q, int r) {

    int i = 0;
    int j = 0;
    int k = 0;

    int *tmp = malloc(sizeof(int) * (q-p+1));

    while ((i<(r-p+1)) || (j < (q-r))) {
        if (i == (r-p+1)) {
            tmp[k] = a[r+1+j];
            j++;
        } else if (j == (q-r)) {
            tmp[k] = a[p+i];
            i++;
        } else {
            if (a[p+i] < a[r+1+j]) {
                tmp[k] = a[p+i];
                i++;
            } else {
                tmp[k] = a[r+1+j];
                j++;
            }
        }
        k++;
    }

    for (int i = p; i < (q+1); i++)
        a[i] = tmp[i-p];
}

void merge_sort(int *a, int p, int q) {
    if (p >= q) {
        return;
    }

    int r = (int)((p+q)/2);
    merge_sort(a, p, r);
    merge_sort(a, r+1, q);
    merge(a, p, q, r);
}

int main() {

    merge_sort(a, 0, N-1);
    for (int i = 0; i < N; i++)
        printf("%d, ", a[i]);

    return 0;
}