package com.caoxin.heap;

public class Heap {
    private int capacity = 0;
    private int[] data = null;
    private int pos = 0;

    public Heap(int capacity) {
        this.capacity = capacity;
        this.data = new int[capacity + 1];
    }

    public int[] getData() {
        return data;
    }

    public void insert(int num) {
        if (pos >= capacity) {
            System.out.println("heap is full");
            return;
        }

        data[++pos] = num;
        int i = pos;
        while (true) {
            if ((i/2) >= 1) {
                if ((data[i] > data[i/2])) {
                    int tmp = data[i];
                    data[i] = data[i/2];
                    data[i/2] = tmp;
                }
                i = i / 2;
            } else {
                break;
            }

        }
    }

    private static void swap(int[] nums, int length, int i) {
        while (true) {
            int max_pos = i;
            if ((i*2 + 1) <= (length-1) && (nums[i] < nums[i*2+1]))
                max_pos = i * 2 + 1;
            if ((i*2 + 2) <= (length-1) && (nums[max_pos] < nums[i*2+2]))
                max_pos = i *2 + 2;

            if (max_pos == i)
                break;
            
            int tmp = nums[i];
            nums[i] = nums[max_pos];
            nums[max_pos] = tmp;

            i = max_pos;
        }
    }

    private static void heaplify(int[] nums, int length) {

        for (int i = (length/2-1); i >= 0; i--) {
            swap(nums, length, i);
        }
    }

    public static void sort(int[] nums) {
        heaplify(nums, nums.length);

        for (int i = nums.length-1; i >= 0; i--) {
            int tmp = nums[0];
            nums[0] = nums[i];
            nums[i] = tmp;

            heaplify(nums, i);
        }
    }

    public static void main(String[] args) {
        System.out.println("in heap class");

        int[] nums = {1, 4, 7, 5, 2, 9, 8};
        // Heap heap = new Heap(7);
        // for (int num : nums) {
        //     System.out.println("insert : " + num);
        //     heap.insert(num);
        // }

        // int[] data = heap.getData();
        // for (int num : data) {
        //     System.out.println("data : " + num);
        // }
        Heap.sort(nums);
        for (int num : nums) {
            System.out.println("data : " + num);
        }
    }

}

