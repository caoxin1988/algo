#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define N 10
int a[N] = {1, 6, 3, 8, 15, 6, 7, 3, 12, 10};

int find_element(int *a, int p, int q, int k) {

    int element = -1;
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

    if (j > (k-1))
        element = find_element(a, p, j-1, k);
    else if (j < (k-1))
        element = find_element(a, j+1, q, k);
    else
        element = a[j];
    
    return element;

}

int main() {
    int ret = find_element(a, 0, N-1, 9);
    printf("element is %d\n", ret);
    return 0;
}