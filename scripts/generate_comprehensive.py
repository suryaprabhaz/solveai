import os
import json

# Comprehensive academic problems covering all specified curriculum topics
CURRICULUM_DATA = [
    # ------------------ C++ (Advanced STL & DSA) ------------------
    {
        "id": "cpp-stack-stl", "title": "Stack in C++ STL", "question": "Implement stack operations using std::stack in C++",
        "language": "cpp", "subject": "Data Structures & Algorithms", "topic": "Stack", "subtopic": "STL",
        "difficulty": "Easy", "time_complexity": "O(1)", "space_complexity": "O(n)",
        "keywords": "stack stl stack in cpp std stack",
        "code": """#include <iostream>
#include <stack>

int main() {
    std::stack<int> s;
    s.push(10); s.push(20); s.push(30);
    std::cout << "Top: " << s.top() << "\\n";
    s.pop();
    std::cout << "Top after pop: " << s.top() << "\\n";
    return 0;
}"""
    },
    {
        "id": "cpp-queue-stl", "title": "Queue in C++ STL", "question": "Implement FIFO queue using std::queue in C++",
        "language": "cpp", "subject": "Data Structures & Algorithms", "topic": "Queue", "subtopic": "STL",
        "difficulty": "Easy", "time_complexity": "O(1)", "space_complexity": "O(n)",
        "keywords": "queue stl queue in cpp std queue",
        "code": """#include <iostream>
#include <queue>

int main() {
    std::queue<std::string> q;
    q.push("First"); q.push("Second"); q.push("Third");
    while (!q.empty()) {
        std::cout << q.front() << " ";
        q.pop();
    }
    std::cout << "\\n";
    return 0;
}"""
    },
    {
        "id": "cpp-priority-queue-heap", "title": "Priority Queue (Max Heap / Min Heap) in C++", "question": "Implement Min-Heap and Max-Heap using std::priority_queue in C++",
        "language": "cpp", "subject": "Data Structures & Algorithms", "topic": "Heap", "subtopic": "Priority Queue",
        "difficulty": "Medium", "time_complexity": "O(log n) push/pop", "space_complexity": "O(n)",
        "keywords": "priority queue heap cpp min heap max heap",
        "code": """#include <iostream>
#include <queue>
#include <vector>

int main() {
    // Max Heap
    std::priority_queue<int> maxH;
    maxH.push(10); maxH.push(30); maxH.push(20);
    std::cout << "Max Heap Top: " << maxH.top() << "\\n";

    // Min Heap
    std::priority_queue<int, std::vector<int>, std::greater<int>> minH;
    minH.push(10); minH.push(30); minH.push(20);
    std::cout << "Min Heap Top: " << minH.top() << "\\n";
    return 0;
}"""
    },
    {
        "id": "cpp-map-unordered-map", "title": "Frequency Counter using std::unordered_map in C++", "question": "Count frequency of elements in an array using hash map",
        "language": "cpp", "subject": "Data Structures & Algorithms", "topic": "Hashing", "subtopic": "Map",
        "difficulty": "Easy", "time_complexity": "O(n)", "space_complexity": "O(n)",
        "keywords": "hash map frequency counter cpp unordered_map",
        "code": """#include <iostream>
#include <vector>
#include <unordered_map>

int main() {
    std::vector<int> arr = {1, 2, 2, 3, 1, 4, 2, 5};
    std::unordered_map<int, int> freq;
    for (int x : arr) freq[x]++;
    for (auto& pair : freq) {
        std::cout << pair.first << ": " << pair.second << "\\n";
    }
    return 0;
}"""
    },
    {
        "id": "cpp-kruskal-mst", "title": "Kruskal Minimum Spanning Tree Algorithm in C++", "question": "Implement Kruskal's algorithm using Disjoint Set Union (DSU)",
        "language": "cpp", "subject": "Data Structures & Algorithms", "topic": "Greedy Algorithms", "subtopic": "MST",
        "difficulty": "Hard", "time_complexity": "O(E log E)", "space_complexity": "O(V + E)",
        "keywords": "kruskal mst kruskal algorithm cpp minimum spanning tree",
        "code": """#include <iostream>
#include <vector>
#include <algorithm>

struct Edge { int u, v, w; };

struct DSU {
    std::vector<int> parent;
    DSU(int n) : parent(n) { for (int i = 0; i < n; i++) parent[i] = i; }
    int find(int i) { return (parent[i] == i) ? i : (parent[i] = find(parent[i])); }
    void unite(int i, int j) { parent[find(i)] = find(j); }
};

int main() {
    int V = 4;
    std::vector<Edge> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    std::sort(edges.begin(), edges.end(), [](Edge a, Edge b) { return a.w < b.w; });
    DSU dsu(V);
    int mst_weight = 0;
    for (auto& e : edges) {
        if (dsu.find(e.u) != dsu.find(e.v)) {
            dsu.unite(e.u, e.v);
            mst_weight += e.w;
        }
    }
    std::cout << "MST Weight: " << mst_weight << "\\n";
    return 0;
}"""
    },
    {
        "id": "cpp-01-knapsack-dp", "title": "0/1 Knapsack Problem using Dynamic Programming in C++", "question": "Solve the 0/1 Knapsack problem with dynamic programming table",
        "language": "cpp", "subject": "Algorithms", "topic": "Dynamic Programming", "subtopic": "Knapsack",
        "difficulty": "Medium", "time_complexity": "O(n * W)", "space_complexity": "O(n * W)",
        "keywords": "0/1 knapsack knapsack dp cpp dynamic programming knapsack",
        "code": """#include <iostream>
#include <vector>
#include <algorithm>

int knapSack(int W, const std::vector<int>& wt, const std::vector<int>& val, int n) {
    std::vector<std::vector<int>> K(n + 1, std::vector<int>(W + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (wt[i - 1] <= w)
                K[i][w] = std::max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
            else
                K[i][w] = K[i - 1][w];
        }
    }
    return K[n][W];
}

int main() {
    std::vector<int> val = {60, 100, 120};
    std::vector<int> wt = {10, 20, 30};
    int W = 50;
    std::cout << "Max Knapsack value: " << knapSack(W, wt, val, val.size()) << "\\n";
    return 0;
}"""
    },

    # ------------------ JAVA (OOP, Collections, Concurrency) ------------------
    {
        "id": "java-linkedlist-custom", "title": "Singly Linked List Implementation in Java", "question": "Implement singly linked list insertion, deletion, and printing in Java",
        "language": "java", "subject": "Data Structures & Algorithms", "topic": "Linked List", "subtopic": "Singly",
        "difficulty": "Medium", "time_complexity": "O(1) insert", "space_complexity": "O(n)",
        "keywords": "linked list java singly linked list java",
        "code": """public class LinkedListCustom {
    static class Node {
        int data; Node next;
        Node(int d) { data = d; next = null; }
    }
    Node head;
    public void insert(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }
    public void print() {
        Node curr = head;
        while (curr != null) {
            System.out.print(curr.data + " -> ");
            curr = curr.next;
        }
        System.out.println("null");
    }
    public static void main(String[] args) {
        LinkedListCustom list = new LinkedListCustom();
        list.insert(10); list.insert(20); list.insert(30);
        list.print();
    }
}"""
    },
    {
        "id": "java-hashmap-operations", "title": "HashMap CRUD Operations in Java", "question": "Write a Java program demonstrating put, get, remove, and containsKey in HashMap",
        "language": "java", "subject": "Data Structures & Algorithms", "topic": "Collections", "subtopic": "HashMap",
        "difficulty": "Easy", "time_complexity": "O(1) average", "space_complexity": "O(n)",
        "keywords": "hashmap java hashmap operations map in java",
        "code": """import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        map.put("Roll_01", 85);
        map.put("Roll_02", 92);
        System.out.println("Roll_01 score: " + map.get("Roll_01"));
        System.out.println("Contains Roll_02: " + map.containsKey("Roll_02"));
        map.remove("Roll_01");
        System.out.println("Size after removal: " + map.size());
    }
}"""
    },
    {
        "id": "java-binary-search", "title": "Binary Search in Java", "question": "Implement iterative binary search on sorted array in Java",
        "language": "java", "subject": "Data Structures & Algorithms", "topic": "Searching", "subtopic": "Binary Search",
        "difficulty": "Easy", "time_complexity": "O(log n)", "space_complexity": "O(1)",
        "keywords": "binary search java binary search in java",
        "code": """public class BinarySearch {
    public static int search(int[] arr, int target) {
        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] == target) return mid;
            if (arr[mid] < target) l = mid + 1;
            else r = mid - 1;
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] data = {2, 4, 6, 8, 10, 12, 14};
        System.out.println("Index of 10: " + search(data, 10));
    }
}"""
    },
    {
        "id": "java-synchronized-counter", "title": "Thread Synchronization with Synchronized Method in Java", "question": "Demonstrate thread safety using synchronized keyword in Java",
        "language": "java", "subject": "Operating Systems & Concurrency", "topic": "Synchronization", "subtopic": "Threads",
        "difficulty": "Medium", "time_complexity": "O(n)", "space_complexity": "O(1)",
        "keywords": "synchronized java thread synchronization counter thread safety",
        "code": """class Counter {
    private int count = 0;
    public synchronized void increment() { count++; }
    public int getCount() { return count; }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Counter c = new Counter();
        Thread t1 = new Thread(() -> { for(int i=0; i<1000; i++) c.increment(); });
        Thread t2 = new Thread(() -> { for(int i=0; i<1000; i++) c.increment(); });
        t1.start(); t2.start();
        t1.join(); t2.join();
        System.out.println("Final Count: " + c.getCount());
    }
}"""
    },

    # ------------------ PYTHON (AI, ML, EDA, OS, Networks) ------------------
    {
        "id": "py-bfs-graph-traversal", "title": "Breadth First Search (BFS) in Python", "question": "Implement Breadth First Search for a graph using collections.deque",
        "language": "python", "subject": "Artificial Intelligence & DSA", "topic": "Graph Algorithms", "subtopic": "BFS",
        "difficulty": "Easy", "time_complexity": "O(V + E)", "space_complexity": "O(V)",
        "keywords": "bfs in python breadth first search python bfs graph",
        "code": """from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': ['F'], 'F': []
}
print("BFS Traversal:", bfs(graph, 'A'))"""
    },
    {
        "id": "py-dfs-graph-traversal", "title": "Depth First Search (DFS) in Python", "question": "Implement Depth First Search for a graph using recursion in Python",
        "language": "python", "subject": "Artificial Intelligence & DSA", "topic": "Graph Algorithms", "subtopic": "DFS",
        "difficulty": "Easy", "time_complexity": "O(V + E)", "space_complexity": "O(V)",
        "keywords": "dfs in python depth first search python dfs graph",
        "code": """def dfs(graph, node, visited=None):
    if visited is None:
        visited = []
    if node not in visited:
        visited.append(node)
        for neighbor in graph.get(node, []):
            dfs(graph, neighbor, visited)
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
print("DFS Traversal:", dfs(graph, 'A'))"""
    },
    {
        "id": "py-astar-search", "title": "A* (A-Star) Search Algorithm in Python", "question": "Implement A* Pathfinding search algorithm on a grid using heapq",
        "language": "python", "subject": "Artificial Intelligence", "topic": "Search Algorithms", "subtopic": "A* Search",
        "difficulty": "Hard", "time_complexity": "O(b^d)", "space_complexity": "O(b^d)",
        "keywords": "a star algorithm a* in python astar pathfinding ai search",
        "code": """import heapq

def a_star(start, goal, neighbors_fn, h_fn):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in neighbors_fn(current):
            tentative_g = g_score[current] + cost
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h_fn(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
    return None

# Simple Manhattan distance heuristic
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

print("A* Search engine initialized successfully.")"""
    },
    {
        "id": "py-knn-classifier", "title": "k-Nearest Neighbors (k-NN) from Scratch in Python", "question": "Implement k-NN classification algorithm using Euclidean distance and NumPy",
        "language": "python", "subject": "Machine Learning", "topic": "Classification", "subtopic": "k-NN",
        "difficulty": "Medium", "time_complexity": "O(n * d)", "space_complexity": "O(n)",
        "keywords": "knn from scratch knn in python k nearest neighbors machine learning",
        "code": """import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = np.array(X)
        self.y_train = np.array(y)

    def predict(self, X):
        return [self._predict(x) for x in np.array(X)]

    def _predict(self, x):
        distances = np.linalg.norm(self.X_train - x, axis=1)
        k_indices = np.argsort(distances)[:self.k]
        k_labels = [self.y_train[i] for i in k_indices]
        return Counter(k_labels).most_common(1)[0][0]

X_train = [[1, 2], [2, 3], [3, 3], [6, 7], [7, 8]]
y_train = [0, 0, 0, 1, 1]
clf = KNN(k=3)
clf.fit(X_train, y_train)
print("Prediction for [2, 2]:", clf.predict([[2, 2]]))"""
    },
    {
        "id": "py-bankers-algorithm", "title": "Banker's Algorithm for Deadlock Avoidance in Python", "question": "Write a Python program to determine whether a system is in a safe state using Banker's Algorithm",
        "language": "python", "subject": "Operating Systems", "topic": "Deadlock", "subtopic": "Banker's Algorithm",
        "difficulty": "Hard", "time_complexity": "O(n^2 * m)", "space_complexity": "O(n * m)",
        "keywords": "bankers algorithm banker algorithm in python deadlock avoidance os",
        "code": """def is_safe_state(processes, available, max_res, allocation):
    n = len(processes)
    m = len(available)
    need = [[max_res[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    safe_seq = []
    work = list(available)

    while len(safe_seq) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m): work[j] += allocation[i][j]
                finish[i] = True
                safe_seq.append(processes[i])
                found = True
        if not found:
            return False, []
    return True, safe_seq

procs = ['P0', 'P1', 'P2', 'P3', 'P4']
avail = [3, 3, 2]
max_r = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

safe, seq = is_safe_state(procs, avail, max_r, alloc)
print("Safe State:", safe, "| Sequence:", " -> ".join(seq))"""
    },
    {
        "id": "py-lru-page-replacement", "title": "LRU Page Replacement Algorithm in Python", "question": "Simulate Least Recently Used (LRU) Page Replacement algorithm and compute page faults",
        "language": "python", "subject": "Operating Systems", "topic": "Memory Management", "subtopic": "Page Replacement",
        "difficulty": "Medium", "time_complexity": "O(n * frames)", "space_complexity": "O(frames)",
        "keywords": "lru page replacement lru in python page faults os simulation",
        "code": """def lru_page_replacement(pages, capacity):
    memory = []
    faults = 0
    for page in pages:
        if page not in memory:
            if len(memory) == capacity:
                memory.pop(0) # Evict LRU
            memory.append(page)
            faults += 1
        else:
            memory.remove(page)
            memory.append(page) # Update usage
    return faults

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
print("Total LRU Page Faults:", lru_page_replacement(pages, 4))"""
    },

    # ------------------ MATLAB / SCIENTIFIC ------------------
    {
        "id": "matlab-matrix-operations", "title": "Matrix Operations and Eigenvalues in MATLAB", "question": "Perform matrix inversion, determinant, and eigenvalue decomposition in MATLAB",
        "language": "matlab", "subject": "Linear Algebra & Scientific Computing", "topic": "Matrices", "subtopic": "Eigenvalues",
        "difficulty": "Easy", "time_complexity": "O(n^3)", "space_complexity": "O(n^2)",
        "keywords": "matlab matrix eigenvalues matlab inverse matrix operations matlab",
        "code": """% Define Matrix
A = [4 -2; 1 1];

% Determinant and Inverse
det_A = det(A);
inv_A = inv(A);

% Eigenvalues and Eigenvectors
[V, D] = eig(A);

disp('Determinant:'); disp(det_A);
disp('Eigenvalues:'); disp(diag(D));
disp('Eigenvectors:'); disp(V);"""
    },
    {
        "id": "matlab-fourier-transform", "title": "Fast Fourier Transform (FFT) in MATLAB", "question": "Compute and plot the FFT of a noisy sinusoidal signal in MATLAB",
        "language": "matlab", "subject": "Signals & Systems", "topic": "Fourier Analysis", "subtopic": "FFT",
        "difficulty": "Medium", "time_complexity": "O(N log N)", "space_complexity": "O(N)",
        "keywords": "fft in matlab fast fourier transform matlab signal processing",
        "code": """Fs = 1000;            % Sampling frequency
T = 1/Fs;             % Sampling period
L = 1500;             % Length of signal
t = (0:L-1)*T;        % Time vector

% Form 50Hz and 120Hz sin waves with noise
S = 0.7*sin(2*pi*50*t) + sin(2*pi*120*t);
X = S + 2*randn(size(t));

% Fast Fourier Transform
Y = fft(X);
P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;

plot(f, P1);
title('Single-Sided Amplitude Spectrum of X(t)');
xlabel('f (Hz)'); ylabel('|P1(f)|'); grid on;"""
    },

    # ------------------ COMPILER DESIGN & THEORY OF COMPUTATION ------------------
    {
        "id": "cd-lexical-analyzer-tokenizer", "title": "Lexical Analyzer (Tokenizer) in Python", "question": "Implement a simple Lexical Analyzer to tokenize keywords, identifiers, numbers, and operators",
        "language": "python", "subject": "Compiler Design", "topic": "Lexical Analysis", "subtopic": "Tokenization",
        "difficulty": "Medium", "time_complexity": "O(n)", "space_complexity": "O(tokens)",
        "keywords": "lexical analyzer compiler design tokenizer in python lexical analysis",
        "code": """import re

TOKEN_SPEC = [
    ('NUMBER',   r'\\d+(\\.\\d*)?'),
    ('KEYWORD',  r'\\b(if|else|while|return|int|float)\\b'),
    ('IDENT',    r'[A-Za-z_][A-Za-z_0-9]*'),
    ('OP',       r'[+\\-*\\/=<>]'),
    ('SKIP',     r'[ \\t\\n]+'),
    ('MISMATCH', r'.'),
]

def tokenize(code):
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)
    tokens = []
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind != 'SKIP':
            tokens.append((kind, value))
    return tokens

code_sample = "int x = 42 + y;"
print("Tokens:", tokenize(code_sample))"""
    },
    {
        "id": "toc-dfa-simulation", "title": "Deterministic Finite Automaton (DFA) Simulator in Python", "question": "Simulate DFA that accepts binary strings ending with '01'",
        "language": "python", "subject": "Theory of Computation", "topic": "Finite Automata", "subtopic": "DFA",
        "difficulty": "Easy", "time_complexity": "O(n)", "space_complexity": "O(1)",
        "keywords": "dfa in python deterministic finite automaton toc theory of computation",
        "code": """def simulate_dfa(string):
    # DFA states: q0 (start), q1 (seen 0), q2 (accepted, seen 01)
    state = 'q0'
    transitions = {
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q1', '1': 'q2'},
        'q2': {'0': 'q1', '1': 'q0'}
    }
    for char in string:
        if char not in ('0', '1'): return False
        state = transitions[state][char]
    return state == 'q2'

print("DFA accepts 1101:", simulate_dfa("1101"))
print("DFA accepts 1100:", simulate_dfa("1100"))"""
    },

    # ------------------ COMPUTER GRAPHICS ------------------
    {
        "id": "cg-dda-line-algorithm", "title": "DDA Line Drawing Algorithm in C/C++", "question": "Implement DDA (Digital Differential Analyzer) line drawing algorithm",
        "language": "c", "subject": "Computer Graphics", "topic": "Rasterization", "subtopic": "Line Drawing",
        "difficulty": "Easy", "time_complexity": "O(dx)", "space_complexity": "O(1)",
        "keywords": "dda line drawing dda algorithm in c computer graphics dda",
        "code": """#include <stdio.h>
#include <math.h>

void drawLineDDA(int x0, int y0, int x1, int y1) {
    int dx = x1 - x0, dy = y1 - y0;
    int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);
    float xInc = (float)dx / steps, yInc = (float)dy / steps;
    float x = x0, y = y0;
    for (int i = 0; i <= steps; i++) {
        printf("Plot Pixel: (%d, %d)\\n", (int)round(x), (int)round(y));
        x += xInc;
        y += yInc;
    }
}

int main() {
    drawLineDDA(2, 3, 9, 8);
    return 0;
}"""
    },
    {
        "id": "cg-bresenham-circle-algorithm", "title": "Bresenham Circle Drawing Algorithm in C", "question": "Implement Midpoint / Bresenham's circle drawing algorithm using 8-way symmetry",
        "language": "c", "subject": "Computer Graphics", "topic": "Rasterization", "subtopic": "Circle Drawing",
        "difficulty": "Medium", "time_complexity": "O(r)", "space_complexity": "O(1)",
        "keywords": "bresenham circle circle drawing algorithm computer graphics midpoint circle",
        "code": """#include <stdio.h>

void plotCirclePoints(int xc, int yc, int x, int y) {
    printf("(%d, %d) ", xc + x, yc + y);
    printf("(%d, %d) ", xc - x, yc + y);
    printf("(%d, %d) ", xc + x, yc - y);
    printf("(%d, %d)\\n", xc - x, yc - y);
}

void bresenhamCircle(int xc, int yc, int r) {
    int x = 0, y = r;
    int d = 3 - 2 * r;
    while (y >= x) {
        plotCirclePoints(xc, yc, x, y);
        x++;
        if (d > 0) { y--; d = d + 4 * (x - y) + 10; }
        else { d = d + 4 * x + 6; }
    }
}

int main() {
    bresenhamCircle(0, 0, 5);
    return 0;
}"""
    }
]

def export_curriculum_ext():
    os.makedirs('data/batches', exist_ok=True)
    path = 'data/batches/batch_08_comprehensive_btech.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(CURRICULUM_DATA, f, indent=2)
    print(f"Generated {len(CURRICULUM_DATA)} items into {path}")

if __name__ == '__main__':
    export_curriculum_ext()
