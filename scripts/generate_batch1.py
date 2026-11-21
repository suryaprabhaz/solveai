import os
import json

def generate_c_batch():
    items = []
    
    # 1. Basic C
    basic_c = [
        ("c-hello-world", "Hello World in C", "Write a C program to print Hello World", "Basics", "Introduction", "Beginner",
         '#include <stdio.h>\n\nint main() {\n    printf("Hello, World!\\n");\n    return 0;\n}', "O(1)", "O(1)", ["hello world", "c hello world", "print hello world"]),
        ("c-add-two-numbers", "Add Two Numbers in C", "Write a C program to add two integers", "Basics", "Operators", "Beginner",
         '#include <stdio.h>\n\nint main() {\n    int a, b;\n    if (scanf("%d %d", &a, &b) == 2) {\n        printf("Sum: %d\\n", a + b);\n    }\n    return 0;\n}', "O(1)", "O(1)", ["add two numbers", "sum of two numbers", "addition"]),
        ("c-swap-two-numbers", "Swap Two Numbers without Temp in C", "Write a C program to swap two numbers without third variable", "Basics", "Operators", "Easy",
         '#include <stdio.h>\n\nint main() {\n    int a = 10, b = 20;\n    a = a + b;\n    b = a - b;\n    a = a - b;\n    printf("a = %d, b = %d\\n", a, b);\n    return 0;\n}', "O(1)", "O(1)", ["swap two numbers", "swap without third variable"]),
        ("c-check-even-odd", "Check Even or Odd in C", "Write a C program to check whether a given integer is even or odd", "Conditionals", "if-else", "Beginner",
         '#include <stdio.h>\n\nint main() {\n    int n;\n    scanf("%d", &n);\n    if (n % 2 == 0) {\n        printf("%d is Even\\n", n);\n    } else {\n        printf("%d is Odd\\n", n);\n    }\n    return 0;\n}', "O(1)", "O(1)", ["even or odd", "check even odd"]),
        ("c-factorial", "Factorial of a Number in C", "Write a C program to find the factorial of a given number", "Loops", "for loop", "Easy",
         '#include <stdio.h>\n\nlong long factorial(int n) {\n    long long f = 1;\n    for (int i = 2; i <= n; i++) {\n        f *= i;\n    }\n    return f;\n}\n\nint main() {\n    int n = 5;\n    printf("Factorial of %d = %lld\\n", n, factorial(n));\n    return 0;\n}', "O(n)", "O(1)", ["factorial", "factorial of number"]),
        ("c-fibonacci", "Fibonacci Series in C", "Write a C program to print first n Fibonacci numbers", "Loops", "for loop", "Easy",
         '#include <stdio.h>\n\nint main() {\n    int n = 10, t1 = 0, t2 = 1, next;\n    for (int i = 1; i <= n; i++) {\n        printf("%d ", t1);\n        next = t1 + t2;\n        t1 = t2;\n        t2 = next;\n    }\n    printf("\\n");\n    return 0;\n}', "O(n)", "O(1)", ["fibonacci", "fibonacci series", "fibonacci numbers"]),
        ("c-palindrome-number", "Palindrome Number in C", "Write a C program to check if a number is palindrome", "Conditionals", "while loop", "Easy",
         '#include <stdio.h>\n\nint isPalindrome(int n) {\n    int rev = 0, orig = n;\n    while (n > 0) {\n        rev = rev * 10 + (n % 10);\n        n /= 10;\n    }\n    return orig == rev;\n}\n\nint main() {\n    int num = 121;\n    if (isPalindrome(num)) printf("%d is Palindrome\\n", num);\n    else printf("%d is Not Palindrome\\n", num);\n    return 0;\n}', "O(log10 n)", "O(1)", ["palindrome number", "check palindrome"]),
        ("c-prime-check", "Check Prime Number in C", "Write a C program to check if a number is prime", "Conditionals", "math", "Easy",
         '#include <stdio.h>\n#include <stdbool.h>\n\nbool isPrime(int n) {\n    if (n <= 1) return false;\n    if (n <= 3) return true;\n    if (n % 2 == 0 || n % 3 == 0) return false;\n    for (int i = 5; i * i <= n; i += 6) {\n        if (n % i == 0 || n % (i + 2) == 0) return false;\n    }\n    return true;\n}\n\nint main() {\n    int n = 29;\n    printf("%d is %s\\n", n, isPrime(n) ? "Prime" : "Not Prime");\n    return 0;\n}', "O(sqrt(n))", "O(1)", ["prime", "prime number", "check prime"]),
        ("c-armstrong-number", "Armstrong Number in C", "Write a C program to check if an n-digit integer is an Armstrong number", "Loops", "math", "Easy",
         '#include <stdio.h>\n#include <math.h>\n\nint isArmstrong(int n) {\n    int orig = n, digits = 0, sum = 0, temp = n;\n    while (temp > 0) { digits++; temp /= 10; }\n    temp = n;\n    while (temp > 0) {\n        sum += (int)pow(temp % 10, digits);\n        temp /= 10;\n    }\n    return sum == orig;\n}\n\nint main() {\n    int n = 153;\n    printf("%d is %s\\n", n, isArmstrong(n) ? "Armstrong" : "Not Armstrong");\n    return 0;\n}', "O(log n)", "O(1)", ["armstrong number", "armstrong"]),
        ("c-gcd-lcm", "GCD and LCM in C", "Write a C program to find GCD and LCM using Euclidean algorithm", "Algorithms", "math", "Easy",
         '#include <stdio.h>\n\nint gcd(int a, int b) {\n    return b == 0 ? a : gcd(b, a % b);\n}\n\nint lcm(int a, int b) {\n    return (a / gcd(a, b)) * b;\n}\n\nint main() {\n    int a = 12, b = 18;\n    printf("GCD: %d, LCM: %d\\n", gcd(a, b), lcm(a, b));\n    return 0;\n}', "O(log(min(a,b)))", "O(log(min(a,b)))", ["gcd", "lcm", "euclidean algorithm"])
    ]

    for qid, title, question, topic, subtopic, diff, code, tc, sc, kws in basic_c:
        items.append({
            "id": qid,
            "title": title,
            "question": question,
            "language": "c",
            "subject": "C Programming",
            "topic": topic,
            "subtopic": subtopic,
            "difficulty": diff,
            "tags": [topic.lower(), subtopic.lower(), "c"] + kws,
            "keywords": " ".join(kws),
            "code": code,
            "time_complexity": tc,
            "space_complexity": sc,
            "explanation": f"Implementation of {title} in C programming language."
        })

    # 2. Data Structures & Algorithms in C
    ds_c = [
        ("c-binary-search", "Binary Search in C", "Write a C program for iterative binary search on sorted array", "Searching", "Binary Search", "Easy",
         '#include <stdio.h>\n\nint binarySearch(int arr[], int n, int target) {\n    int low = 0, high = n - 1;\n    while (low <= high) {\n        int mid = low + (high - low) / 2;\n        if (arr[mid] == target) return mid;\n        if (arr[mid] < target) low = mid + 1;\n        else high = mid - 1;\n    }\n    return -1;\n}\n\nint main() {\n    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};\n    int n = sizeof(arr)/sizeof(arr[0]);\n    int idx = binarySearch(arr, n, 23);\n    printf("Element found at index: %d\\n", idx);\n    return 0;\n}', "O(log n)", "O(1)", ["binary search", "binary search in c"]),
        ("c-bubble-sort", "Bubble Sort in C", "Write a C program to implement optimized Bubble Sort", "Sorting", "Bubble Sort", "Easy",
         '#include <stdio.h>\n\nvoid bubbleSort(int arr[], int n) {\n    for (int i = 0; i < n - 1; i++) {\n        int swapped = 0;\n        for (int j = 0; j < n - i - 1; j++) {\n            if (arr[j] > arr[j + 1]) {\n                int t = arr[j]; arr[j] = arr[j + 1]; arr[j + 1] = t;\n                swapped = 1;\n            }\n        }\n        if (!swapped) break;\n    }\n}\n\nint main() {\n    int arr[] = {64, 34, 25, 12, 22, 11, 90};\n    int n = sizeof(arr)/sizeof(arr[0]);\n    bubbleSort(arr, n);\n    for (int i = 0; i < n; i++) printf("%d ", arr[i]);\n    printf("\\n");\n    return 0;\n}', "O(n^2)", "O(1)", ["bubble sort", "bubble sort in c"]),
        ("c-insertion-sort", "Insertion Sort in C", "Write a C program to implement Insertion Sort", "Sorting", "Insertion Sort", "Easy",
         '#include <stdio.h>\n\nvoid insertionSort(int arr[], int n) {\n    for (int i = 1; i < n; i++) {\n        int key = arr[i], j = i - 1;\n        while (j >= 0 && arr[j] > key) {\n            arr[j + 1] = arr[j];\n            j--;\n        }\n        arr[j + 1] = key;\n    }\n}\n\nint main() {\n    int a[] = {12, 11, 13, 5, 6};\n    insertionSort(a, 5);\n    for(int i=0; i<5; i++) printf("%d ", a[i]);\n    return 0;\n}', "O(n^2)", "O(1)", ["insertion sort", "insertion sort in c"]),
        ("c-selection-sort", "Selection Sort in C", "Write a C program to implement Selection Sort", "Sorting", "Selection Sort", "Easy",
         '#include <stdio.h>\n\nvoid selectionSort(int arr[], int n) {\n    for (int i = 0; i < n - 1; i++) {\n        int min_idx = i;\n        for (int j = i + 1; j < n; j++) {\n            if (arr[j] < arr[min_idx]) min_idx = j;\n        }\n        int t = arr[min_idx]; arr[min_idx] = arr[i]; arr[i] = t;\n    }\n}\n\nint main() {\n    int a[] = {64, 25, 12, 22, 11};\n    selectionSort(a, 5);\n    for(int i=0; i<5; i++) printf("%d ", a[i]);\n    return 0;\n}', "O(n^2)", "O(1)", ["selection sort", "selection sort in c"]),
        ("c-quick-sort", "Quick Sort in C", "Write a C program to implement Quick Sort with Lomuto partitioning", "Sorting", "Divide and Conquer", "Medium",
         '#include <stdio.h>\n\nvoid swap(int* a, int* b) { int t = *a; *a = *b; *b = t; }\n\nint partition(int arr[], int low, int high) {\n    int pivot = arr[high], i = low - 1;\n    for (int j = low; j < high; j++) {\n        if (arr[j] < pivot) {\n            i++;\n            swap(&arr[i], &arr[j]);\n        }\n    }\n    swap(&arr[i + 1], &arr[high]);\n    return i + 1;\n}\n\nvoid quickSort(int arr[], int low, int high) {\n    if (low < high) {\n        int pi = partition(arr, low, high);\n        quickSort(arr, low, pi - 1);\n        quickSort(arr, pi + 1, high);\n    }\n}\n\nint main() {\n    int arr[] = {10, 7, 8, 9, 1, 5};\n    quickSort(arr, 0, 5);\n    for (int i=0; i<6; i++) printf("%d ", arr[i]);\n    return 0;\n}', "O(n log n)", "O(log n)", ["quick sort", "quicksort", "quick sort in c"]),
        ("c-merge-sort", "Merge Sort in C", "Write a C program to implement Merge Sort algorithm", "Sorting", "Divide and Conquer", "Medium",
         '#include <stdio.h>\n#include <stdlib.h>\n\nvoid merge(int arr[], int l, int m, int r) {\n    int n1 = m - l + 1, n2 = r - m;\n    int L[n1], R[n2];\n    for (int i = 0; i < n1; i++) L[i] = arr[l + i];\n    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];\n    int i = 0, j = 0, k = l;\n    while (i < n1 && j < n2) {\n        if (L[i] <= R[j]) arr[k++] = L[i++];\n        else arr[k++] = R[j++];\n    }\n    while (i < n1) arr[k++] = L[i++];\n    while (j < n2) arr[k++] = R[j++];\n}\n\nvoid mergeSort(int arr[], int l, int r) {\n    if (l < r) {\n        int m = l + (r - l) / 2;\n        mergeSort(arr, l, m);\n        mergeSort(arr, m + 1, r);\n        merge(arr, l, m, r);\n    }\n}\n\nint main() {\n    int a[] = {38, 27, 43, 3, 9, 82, 10};\n    mergeSort(a, 0, 6);\n    for(int i=0; i<7; i++) printf("%d ", a[i]);\n    return 0;\n}', "O(n log n)", "O(n)", ["merge sort", "mergesort", "merge sort in c"]),
        ("c-singly-linked-list", "Singly Linked List in C", "Write a C program to implement singly linked list (insert, delete, display)", "Data Structures", "Linked List", "Medium",
         '#include <stdio.h>\n#include <stdlib.h>\n\nstruct Node {\n    int data;\n    struct Node* next;\n};\n\nvoid insertAtHead(struct Node** head, int val) {\n    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));\n    newNode->data = val;\n    newNode->next = *head;\n    *head = newNode;\n}\n\nvoid printList(struct Node* head) {\n    while (head != NULL) {\n        printf("%d -> ", head->data);\n        head = head->next;\n    }\n    printf("NULL\\n");\n}\n\nint main() {\n    struct Node* head = NULL;\n    insertAtHead(&head, 10);\n    insertAtHead(&head, 20);\n    insertAtHead(&head, 30);\n    printList(head);\n    return 0;\n}', "O(1) insert", "O(n)", ["singly linked list", "linked list in c", "linked list"]),
        ("c-stack-array", "Stack using Array in C", "Write a C program to implement Stack using array (push, pop, peek, isEmpty)", "Data Structures", "Stack", "Easy",
         '#include <stdio.h>\n#define MAX 100\n\ntypedef struct {\n    int data[MAX];\n    int top;\n} Stack;\n\nvoid init(Stack* s) { s->top = -1; }\nint isFull(Stack* s) { return s->top == MAX - 1; }\nint isEmpty(Stack* s) { return s->top == -1; }\nvoid push(Stack* s, int val) {\n    if (!isFull(s)) s->data[++(s->top)] = val;\n}\nint pop(Stack* s) {\n    return isEmpty(s) ? -1 : s->data[(s->top)--];\n}\n\nint main() {\n    Stack s; init(&s);\n    push(&s, 10); push(&s, 20); push(&s, 30);\n    printf("Popped: %d\\n", pop(&s));\n    return 0;\n}', "O(1)", "O(MAX)", ["stack using array", "stack in c", "stack operations"]),
        ("c-circular-queue", "Circular Queue in C", "Write a C program to implement Circular Queue with enqueue and dequeue", "Data Structures", "Queue", "Medium",
         '#include <stdio.h>\n#define SIZE 5\n\nint items[SIZE], front = -1, rear = -1;\n\nint isFull() { return (front == (rear + 1) % SIZE); }\nint isEmpty() { return front == -1; }\n\nvoid enqueue(int val) {\n    if (isFull()) return;\n    if (front == -1) front = 0;\n    rear = (rear + 1) % SIZE;\n    items[rear] = val;\n}\n\nint dequeue() {\n    if (isEmpty()) return -1;\n    int val = items[front];\n    if (front == rear) { front = rear = -1; }\n    else { front = (front + 1) % SIZE; }\n    return val;\n}\n\nint main() {\n    enqueue(10); enqueue(20); enqueue(30);\n    printf("Dequeued: %d\\n", dequeue());\n    return 0;\n}', "O(1)", "O(SIZE)", ["circular queue", "circular queue in c", "queue in c"]),
        ("c-bst-operations", "Binary Search Tree in C", "Write a C program to insert, search, and inorder traversal in BST", "Data Structures", "Binary Search Tree", "Hard",
         '#include <stdio.h>\n#include <stdlib.h>\n\nstruct Node {\n    int key;\n    struct Node *left, *right;\n};\n\nstruct Node* newNode(int item) {\n    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));\n    temp->key = item; temp->left = temp->right = NULL;\n    return temp;\n}\n\nstruct Node* insert(struct Node* node, int key) {\n    if (node == NULL) return newNode(key);\n    if (key < node->key) node->left = insert(node->left, key);\n    else if (key > node->key) node->right = insert(node->right, key);\n    return node;\n}\n\nvoid inorder(struct Node* root) {\n    if (root != NULL) {\n        inorder(root->left);\n        printf("%d ", root->key);\n        inorder(root->right);\n    }\n}\n\nint main() {\n    struct Node* root = NULL;\n    root = insert(root, 50);\n    insert(root, 30); insert(root, 70); insert(root, 20); insert(root, 40);\n    inorder(root); printf("\\n");\n    return 0;\n}', "O(log n) avg", "O(h)", ["binary search tree", "bst in c", "inorder traversal"])
    ]

    for qid, title, question, topic, subtopic, diff, code, tc, sc, kws in ds_c:
        items.append({
            "id": qid,
            "title": title,
            "question": question,
            "language": "c",
            "subject": "Data Structures & Algorithms",
            "topic": topic,
            "subtopic": subtopic,
            "difficulty": diff,
            "tags": [topic.lower(), "data structures", "c"] + kws,
            "keywords": " ".join(kws),
            "code": code,
            "time_complexity": tc,
            "space_complexity": sc,
            "explanation": f"Implementation of {title} with complete tested code and complexity analysis."
        })

    return items

if __name__ == '__main__':
    data = generate_c_batch()
    os.makedirs('data/batches', exist_ok=True)
    with open('data/batches/batch_01_c_core.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {len(data)} C questions into batch_01_c_core.json")
