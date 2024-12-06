from sys import stdin

def maximum_gold(capacity, weights):
    value = [[0]*(len(weights) + 1) for _ in range(capacity + 1)]
    for i in range(len(weights)): 
        for w in range(capacity): 
            value[w+1][i+1] = value[w+1][i]
            if weights[i] <= w+1:
                val = value[(w+1) - weights[i]][i] + weights[i]
                if val > value[w+1][i+1]:
                    value[w+1][i+1] = val
    return value[-1][-1]

if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))