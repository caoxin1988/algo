package com.caoxin.sort;

public class KthElement {

    public int findElement(int[] a, int p, int q, int k) {
        int element = -1;

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
        a[q] = a[q];
        a[q] = tmp;

        if (j > (k-1)) {
            element = findElement(a, p, j-1, k);
        } else if (j < (k-1)) {
            element = findElement(a, j+1, q, k);
        } else {
            element = a[j];
        }

        return element;
    }

    public static void main(String[] args) {
        System.out.println("Kth Element");

        int[] a = {11, 4, 7, 5, 2, 9, 5, 3, 10, 5};
        int N = 10;

        KthElement kth = new KthElement();
        int element = kth.findElement(a, 0, N-1, 9);

        System.out.print("kth element : " + element);
        
    }
}
