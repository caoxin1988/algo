package com.caoxin.sort;

public class BaseSort {

    public String[] a = {"153764", "153925", "138725", "158274", "186351"};

    public void baseSort() {
        for (int i = (a[0].length() -1); i >= 0; i--)
            countSort(i);
    }

    private void countSort(int k) {
        int[] counting = new int[10];
        String[] tmp = new String[a.length];

        for (int i = 0; i < a.length; i++) {
            int value = Integer.parseInt(a[i].substring(k, k+1));
            counting[value] += 1;
        }

        for (int i = 1; i < 10; i++) {
            counting[i] += counting[i-1];
        }

        for (int i = (a.length - 1); i >= 0; i--) {
            int value = Integer.parseInt(a[i].substring(k, k+1));
            int j = counting[value];
            tmp[j-1] = a[i];
            counting[value]--;
        }

        for (int i =0; i < a.length; i++) {
            a[i] = tmp[i];
        }
    }

    public static void main(String[] args) {
        System.out.println("Base Sort");

        BaseSort sort = new BaseSort();
        sort.baseSort();

        for (int i =0; i < sort.a.length; i++) {
            System.out.println(sort.a[i]);
        }
    }
}

