#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct list_node {
    int data;
    struct list_node* next;
};

struct list_queue {
    struct list_node* head;
    struct list_node* tail;
};

bool queue_init(struct list_queue* queue) {

    queue->head = NULL;
    queue->tail = NULL;

    return true;
}

bool enqueue(struct list_queue* queue, int data) {

    struct list_node* node = malloc(sizeof(struct list_node));
    node->data = data;

    if (queue->head == NULL) {
        queue->head = node;
        queue->tail = node;
        return true;
    }

    queue->tail->next = node;
    queue->tail = node;

    return true;
}

int dequeue(struct list_queue* queue) {
    if (queue->head == NULL) {
        printf("    ->queue is empty, dequeue fail\n");
        return -1;
    }

    struct list_node* node = queue->head;
    queue->head = queue->head->next;
    int data = node->data;
    free(node);

    return data;
}

int main() {

    struct list_queue queue;

    queue_init(&queue);

    enqueue(&queue, 1);
    enqueue(&queue, 2);
    enqueue(&queue, 3);

    printf("data : %d\n", dequeue(&queue));
    printf("data : %d\n", dequeue(&queue));
    printf("data : %d\n", dequeue(&queue));
    printf("data : %d\n", dequeue(&queue));

    enqueue(&queue, 4);
    printf("data : %d\n", dequeue(&queue));
    printf("data : %d\n", dequeue(&queue));

    return 1;
}