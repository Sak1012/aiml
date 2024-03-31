#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100

struct Node {
    char data;
    struct Node* next;
};

struct Node* createNode(char data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void enqueue(struct Node** front, struct Node** rear, char data) {
    struct Node* newNode = createNode(data);
    if (*rear == NULL) {
        *front = *rear = newNode;
    } else {
        (*rear)->next = newNode;
        *rear = newNode;
    }
}

char dequeue(struct Node** front, struct Node** rear) {
    if (*front == NULL) {
        printf("Queue is empty\n");
        return -1;
    }
    struct Node* temp = *front;
    char data = temp->data;
    *front = (*front)->next;
    if (*front == NULL) {
        *rear = NULL;
    }
    free(temp);
    return data;
}

bool isEmpty(struct Node* front) {
    return front == NULL;
}

void bfs(char start, int graph_size, char graph[][graph_size]) {
    bool visited[MAX_SIZE] = { false };
    struct Node* queueFront = NULL;
    struct Node* queueRear = NULL;

    printf("BFS Traversal: ");
    visited[start - 'A'] = true;
    enqueue(&queueFront, &queueRear, start);

    while (!isEmpty(queueFront)) {
        char current = dequeue(&queueFront, &queueRear);
        printf("%c ", current);

        for (int i = 0; i < graph_size; ++i) {
            if (graph[current - 'A'][i] == 1 && !visited[i]) {
                visited[i] = true;
                enqueue(&queueFront, &queueRear, i + 'A');
            }
        }
    }
    printf("\n");
}

void dfsUtil(char current, bool visited[], int graph_size, char graph[][graph_size]) {
    visited[current - 'A'] = true;
    printf("%c ", current);

    for (int i = 0; i < graph_size; ++i) {
        if (graph[current - 'A'][i] == 1 && !visited[i]) {
            dfsUtil(i + 'A', visited, graph_size, graph);
        }
    }
}

void dfs(char start, int graph_size, char graph[][graph_size]) {
    bool visited[MAX_SIZE] = { false };

    printf("DFS Traversal: ");
    dfsUtil(start, visited, graph_size, graph);
    printf("\n");
}

int main() {
    int graph_size = 6; // number of nodes in the graph
    char graph[][6] = {
        {0, 1, 1, 0, 0, 0},
        {1, 0, 0, 1, 1, 0},
        {1, 0, 0, 0, 0, 1},
        {0, 1, 0, 0, 0, 0},
        {0, 1, 0, 0, 0, 1},
        {0, 0, 1, 0, 1, 0}
    };

    bfs('A', graph_size, graph);
    dfs('A', graph_size, graph);

    return 0;
}

