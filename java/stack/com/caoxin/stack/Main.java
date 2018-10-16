package com.caoxin.stack;

public class Main {
    public static void main( String[] args )
    {
        System.out.println( "array stack program!" );

        // ArrayStack stack = new ArrayStack(10);
        // stack.push(1);
        // stack.push(2);

        // System.out.println("data : " + stack.pop());
        // System.out.println("data : " + stack.pop());
        // System.out.println("data : " + stack.pop());

        // stack.push(3);
        // System.out.println("data : " + stack.pop());
        // System.out.println("data : " + stack.pop());

        System.out.println( "==================" );
        ListStack stack1 = new ListStack();

        stack1.push(1);
        stack1.push(2);
        System.out.println("data : " + stack1.pop());
        System.out.println("data : " + stack1.pop());
        System.out.println("data : " + stack1.pop());

        stack1.push(5);
        System.out.println("data : " + stack1.pop());
        System.out.println("data : " + stack1.pop());

    }
}