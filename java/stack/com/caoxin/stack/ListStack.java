package com.caoxin.stack;

public class ListStack 
{

    private ListNode top = null;

    public ListStack() {
        this.top = null;
    }

    public boolean push(int data) {
        ListNode node = new ListNode(data);
        
        node.prev = this.top;
        this.top = node;
        
        return true;
    }

    public int pop() {
        if (this.top == null) {
            return -1;
        }

        ListNode node = this.top;
        this.top = node.prev;

        return node.getData();
    }
    
    class ListNode {
    
        private int data;
        public ListNode prev;

        public ListNode(int data) {
            this.data = data;
            this.prev = null;
        }

        public int getData() {
            return this.data;
        }
    }

}