package com.caoxin.queue;

public class ArrayQueue {

    private int[] data;
    private int head = 0;
    private int tail = 0;
    private int size = 0;

    public ArrayQueue(int size) {
        this.data = new int[size];
        this.size = size;
        this.head = 0;
        this.tail = 0;
    }

    public boolean enqueue(int data) {

        if (tail == size) {

            if (head == 0) {
                System.out.println("    -> queue is full, enqueue fail");
                return false;
            }

            for (int i = head; i < tail; i++) {
                this.data[i - head] = this.data[i];
            }
            
            tail = tail - head;
            head = 0;
        }

        this.data[tail++] = data;

        return true;

    }

    public int dequeue() {

        if (head == tail) {
            System.out.println("    -> queue is empty, dequeue fail");
            return -1;
        }

        return data[head++];
    }
}