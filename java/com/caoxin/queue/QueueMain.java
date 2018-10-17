package com.caoxin.queue;

public class QueueMain {
    public static void main(String[] args) {
        System.out.println("array queue and list queue!!");

        // ArrayQueue queue = new ArrayQueue(3);
        // queue.enqueue(1);
        // queue.enqueue(2);
        // queue.enqueue(3);
        // queue.enqueue(4);

        // System.out.println("data : " + queue.dequeue());
        // System.out.println("data : " + queue.dequeue());
        // System.out.println("data : " + queue.dequeue());
        // System.out.println("data : " + queue.dequeue());
        // System.out.println("data : " + queue.dequeue());



        // queue.enqueue(2);
        // System.out.println("data : " + queue.dequeue());
        // System.out.println("data : " + queue.dequeue());

        ListQueue queue1 = new ListQueue();
        queue1.enqueue(1);
        queue1.enqueue(2);
        queue1.enqueue(3);

        System.out.println("data : " + queue1.dequeue());
        System.out.println("data : " + queue1.dequeue());
        System.out.println("data : " + queue1.dequeue());
        System.out.println("data : " + queue1.dequeue());


        queue1.enqueue(4);
        System.out.println("data : " + queue1.dequeue());
        System.out.println("data : " + queue1.dequeue());
    }
}