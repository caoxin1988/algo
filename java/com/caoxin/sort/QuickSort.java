package com.caoxin.sort;

public class QuickSort {

    public void quickSort(int[] a, int p, int q) {
        if (p >= q)
            return;
        
        int j = p;
        int pivot = a[q];
        for (int i = p; i <= q; i++) {
            if (a[i] < pivot) {
                int tmp = a[i];
                a[i] = a[j];
                a[j] = tmp;

                j++;
            }
        }

        int tmp = a[j];
        a[j] = a[q];
        a[q] = tmp;

        quickSort(a, p, j-1);
        quickSort(a, j+1, q);
    }
    public static void main(String[] args) {

        int[] a = {11, 4, 7, 5, 2, 9, 5, 3, 10, 5};
        int N = 10;

        System.out.println("Quick Sort");

        QuickSort sort = new QuickSort();
        sort.quickSort(a, 0, N-1);

        for (int i = 0; i < N; i++)
            System.out.println(a[i] + ", ");
        
    }
}