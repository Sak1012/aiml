#include <iostream>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <stack>

using namespace std;

// Function to perform Breadth First Search (BFS)
void bfs(unordered_map<char, vector<char>>& graph, char start) {
    unordered_set<char> visited;
    queue<char> q;

    q.push(start);
    visited.insert(start);

    while (!q.empty()) {
        char current = q.front();
        q.pop();
        cout << current << " ";

        for (char neighbor : graph[current]) {
            if (visited.find(neighbor) == visited.end()) {
                q.push(neighbor);
                visited.insert(neighbor);
            }
        }
    }
}

// Function to perform Depth First Search (DFS)
void dfs(unordered_map<char, vector<char>>& graph, char start) {
    unordered_set<char> visited;
    stack<char> s;

    s.push(start);

    while (!s.empty()) {
        char current = s.top();
        s.pop();

        if (visited.find(current) == visited.end()) {
            cout << current << " ";
            visited.insert(current);

            for (char neighbor : graph[current]) {
                if (visited.find(neighbor) == visited.end()) {
                    s.push(neighbor);
                }
            }
        }
    }
}

int main() {
    unordered_map<char, vector<char>> graph = {
        {'A', {'B', 'C'}},
        {'B', {'A', 'D', 'E'}},
        {'C', {'A', 'F'}},
        {'D', {'B'}},
        {'E', {'B', 'F'}},
        {'F', {'C', 'E'}}
    };

    cout << "BFS Traversal: ";
    bfs(graph, 'A');
    cout << endl;

    cout << "DFS Traversal: ";
    dfs(graph, 'A');
    cout << endl;

    return 0;
}

