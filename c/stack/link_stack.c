#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct link_node {
    unsigned int data;
    struct link_node* prev;
};

struct link_stack {
    struct link_node* top;
};

bool stack_init(struct link_stack* stack) {

    stack->top = NULL;
    return true;
}

bool push(struct link_stack* stack, int data) {

    if (data < 0) {
        printf("invalid data type\n");
        return false;
    }

    struct link_node* node = malloc(sizeof(struct link_node));
    node->data = data;
    node->prev = stack->top;
    stack->top = node;

    return true;
}

int pop(struct link_stack* stack) {

    if (stack->top == NULL) {
        printf("stack is empty, pop fail\n");
        return -1;
    }

    struct link_node* node = stack->top;
    unsigned int data = node->data;
    stack->top = stack->top->prev;
    free(node);

    return data;
}


int main() {
    struct link_stack stack;

    stack_init(&stack);

    push(&stack, 1);
    push(&stack, 2);

    printf("data : %d\n", pop(&stack));
    printf("data : %d\n", pop(&stack));
    printf("data : %d\n", pop(&stack));

    push(&stack, 3);
    printf("data : %d\n", pop(&stack));

    return 1;
}