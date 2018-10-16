package com.caoxin.stack;

public class ArrayStack 
{
    private int[] data;
    private int count;
    private int size;
    
    public ArrayStack(int size) {
        this.data = new int[size];
        this.count = 0;
        this.size = size;
    }

    public boolean push(int data) {
        if (this.count > this.size) {
            System.out.println("stack is full, push fail");
            return false;
        }

        this.data[this.count++] = data;
        return true;
    }

    public int pop() {

        this.count--;
        if (this.count < 0) {
            System.out.println("stack is empty, pop fail");
            this.count = 0;
            return -1;
        }

        return this.data[this.count];
    }
}
