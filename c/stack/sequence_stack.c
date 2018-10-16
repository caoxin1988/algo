#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct array_stack {
    unsigned int *data;
    int count;
    int size;
};

bool init_stack(struct array_stack* stack, int size) {
    stack->data = (int *)malloc(sizeof(int) * size);
    if (stack->data == NULL)
        return false;
    else {
        stack->count = 0;
        stack->size = size;
    }

    return true;
}

bool push(struct array_stack* stack, int data) {

    if (stack->count > stack->size) {
        printf("stack if full, push fail\n");
        return false;
    }

    stack->data[stack->count] = data;
    stack->count++;

    return true;
}

int pop(struct array_stack* stack) {
    struct array_stack node;

    stack->count--;
    if (stack->count < 0) {
        printf("stack is empty, pop fail\n");
        stack->count = 0;
        return -1;
    }

    return stack->data[stack->count];

}

int main() {
    struct array_stack stack;
    bool ret = false;

    ret = init_stack(&stack, 10);
    printf("stack init success\n");

    push(&stack, 1);
    push(&stack, 2);

    printf("data : %d\n", pop(&stack));
    printf("data : %d\n", pop(&stack));
    printf("data : %d\n", pop(&stack));

    push(&stack, 3);
    printf("data : %d\n", pop(&stack));

    return 1;
}