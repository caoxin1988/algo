#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct array_queue {
    int* data;
    int size;
    int head;
    int tail;
};

bool init_queue(struct array_queue* queue, int size) {
    queue->data = malloc(sizeof(int) * size);

    if (queue->data == NULL) {
        printf("data malloc error\n");
        return false;
    }

    queue->size = size;
    queue->head = 0;
    queue->tail = 0;

    return true;
}

bool enqueue(struct array_queue* queue, int data) {

    if (queue->tail == queue->size) {
        if (queue->head == 0) {
            printf("    ->queue is full, enqueue fail\n");
            return false;
        }

        for (int i = 0; i < queue->tail; i++) {
            queue->data[i - queue->head] = queue->data[i];
        }

        queue->tail = queue->tail - queue->head;
        queue->head = 0;
    }

    queue->data[queue->tail++] = data;

    return true;
}

int dequeue(struct array_queue* queue) {
    if (queue->head == queue->tail) {
        printf("    ->queue is empty, dequeue fail\n");
        return -1;
    }

    return queue->data[queue->head++];
}


int main(void) {

    struct array_queue queue;
    
    init_queue(&queue, 3);

    enqueue(&queue, 1);
    enqueue(&queue, 2);
    enqueue(&queue, 3);
    enqueue(&queue, 4);

    printf("data : %d\n", dequeue(&queue));
    printf("data : %d\n", dequeue(&queue));
    printf("data : %d\n", dequeue(&queue));
    printf("data : %d\n", dequeue(&queue));

    enqueue(&queue, 5);
    printf("data : %d\n", dequeue(&queue));
    printf("data : %d\n", dequeue(&queue));


    return 1;
}