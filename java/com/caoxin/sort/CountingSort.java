package com.caoxin.sort;

public class CountingSort {

    public int[] a = {3, 4, 7, 5, 2, 9, 5, 3, 1, 5};

    public void countingSort() {
        int[] counting = new int[10];
        int[] tmp = new int[a.length];

        for (int i = 0; i < tmp.length; i++)
            tmp[i] = 0;

        for (int i = 0; i < a.length; i++) {
            int value = a[i];
            counting[value] += 1;
        }

        for (int i = 1; i < a.length; i++) {
            counting[i] += counting[i-1];
        }

        for (int i = (a.length-1); i >= 0; i--) {
            int value = a[i];
            int j = counting[value];
            tmp[j-1] = value;
            counting[value]--;
        }

        for (int i = 0; i < a.length; i++)
            a[i] = tmp[i];
    }

    public int getLength() {
        return a.length;
    }

    public static void main(String[] args) {
        System.out.println("Counting Sort");

        CountingSort sort = new CountingSort();
        sort.countingSort();

        for (int i =0; i < sort.getLength(); i++)
            System.out.println(sort.a[i] + " ");
    }
}
