import sys
import threading

def compute_height(n, parents):
    T = [None] * n
    root = parents.index(-1)
    T[root] = 1
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
            if T[current]:
                T[vertex] = T[current] + height
                break
    return max(T)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
    sys.setrecursionlimit(10 ** 7)  
threading.stack_size(2 ** 27)  
threading.Thread(target=main).start()