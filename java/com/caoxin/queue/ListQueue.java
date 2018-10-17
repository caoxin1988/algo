package com.caoxin.queue;

public class ListQueue {

    private ListNode head;
    private ListNode tail;

    public ListQueue() {
        head = null;
        tail = null;
    }

    public boolean enqueue(int data) {

        ListNode node = new ListNode(data);

        if (head == null) {
            tail = node;
            head = node;

            return true;
        }

        tail.next = node;
        tail = node;

        return true;
    }

    public int dequeue() {

        if (head == null) {
            System.out.println("    -> queue is empty, dequeue fail");
            return -1;
        }

        ListNode node = head;

        if (head.next == null) {
            head = tail = null;
        } else {
            head = head.next;
        }

        node.next = null;

        return node.getValue();
    }

    class ListNode {

        private int data = -1;
        public ListNode next;

        public ListNode(int data) {
            this.data = data;
            this.next = null;
        }

        public int getValue() {
            return this.data;
        }
    }
}