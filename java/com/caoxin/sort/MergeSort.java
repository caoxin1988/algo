package com.caoxin.sort;

public class MergeSort {

    public void mergeSort(int[] a, int p, int q) {
        if (p >= q) {
            return;
        }

        int r = (int)((p+q)/2);

        mergeSort(a, p, r);
        mergeSort(a, r+1, q);
        merge(a, p, q, r);
    }

    private void merge(int[] a, int p, int q, int r) {
        int i = 0;
        int j = 0;
        int k = 0;
        int[] tmp = new int[q-p+1];

        while ((i < (r-p+1)) || (j < (q-r))) {
            if (i == (r-p+1)) {
                tmp[k++] = a[r+1+j];
                j++;
            } else if (j == (q-r)) {
                tmp[k++] = a[p+i];
                i++;
            } else {
                if (a[p+i] < a[r+1+j]) {
                    tmp[k++] = a[p+i];
                    i++;
                } else {
                    tmp[k++] = a[r+1+j];
                    j++;
                }
            }
        }

        for (int m = p; m <= q; m++)
            a[m] = tmp[m-p];
    }

    public static void main(String[] args) {
        System.out.println("merge sort");

        int[] a = {11, 4, 7, 5, 2, 9, 5, 3, 10, 5};
        int N = 10;

        MergeSort sort = new MergeSort();

        sort.mergeSort(a, 0, N-1);

        for (int i = 0; i < N; i++) {
            System.out.println(a[i] + ", ");
        }
    }
}

