package com.caoxin.sort;

public class Sort {

    private int[] a = {1, 4, 6, 3, 7, 4, 1 ,10, 6 ,4};
    private int n = a.length;

    public void bubbleSort() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < (n-i-1); j++) {
                if (a[j] > a[j+1]) {
                    int tmp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = tmp;
                }
            }
        }

        System.out.println("new array: ");
        for (int i = 0; i < n; i++)
            System.out.println(a[i] + " ");
    }

    // private int[] a = {1, 4, 6, 3, 7, 4, 1 ,10, 6 ,4};
    public void insertSort() {

        for (int i = 1; i < n; i++) {
            int tmp = a[i];
            for (int j = (i-1); j >= 0; j--) {
                if (tmp < a[j]) {
                    a[j+1] = a[j];
                } else {
                    a[j+1] = tmp;
                    break;
                }
            }
        }
        System.out.println("new array: ");
        for (int i = 0; i < n; i++)
            System.out.println(a[i] + " ");

    }

    // private int[] a = {1, 4, 6, 3, 7, 4, 1 ,10, 6 ,4};
    public void selectSort() {
        for (int i = 0; i < n; i++) {
            int min = a[i];
            int t = i;

            for (int j = (i+1); j < n; j++) {
                if (min > a[j]) {
                    min = a[j];
                    t = j;
                }
            }

            if (t != i) {
                a[t] = a[i];
                a[i] = min;
            }
        }

        System.out.println("new array: ");
        for (int i = 0; i < n; i++)
            System.out.println(a[i] + " ");

    }

    public static void main(String[] args) {
        System.out.println("sort algo");

        Sort s = new Sort();
        // s.bubbleSort();
        // s.insertSort();
        s.selectSort();
    }
}

