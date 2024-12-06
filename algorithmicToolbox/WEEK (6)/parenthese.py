import sys


def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_max(i, j, m, M, ops):
    minimum = sys.maxsize 
    maximum = -sys.maxsize 

    for k in range(i, j):
        
        
        
        a = evaluate(M[i][k], M[k+1][j], ops[k])
        b = evaluate(M[i][k], m[k+1][j], ops[k])
        c = evaluate(m[i][k], M[k+1][j], ops[k])
        d = evaluate(m[i][k], m[k+1][j], ops[k])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    
    return minimum, maximum



def maximum_value(dataset):
  
    ops = [dataset[i] for i in range(len(dataset)) if i % 2 != 0]
    nums = [int(dataset[i]) for i in range(len(dataset)) if i % 2 == 0]
    
    m = [[0]*len(nums) for _ in range(len(nums))]
    M = [[0]*len(nums) for _ in range(len(nums))]
    for i in range(len(nums)):
        m[i][i] = nums[i]
        M[i][i] = nums[i]
    
    
    for s in range(1, len(nums)):
        for i in range(0, len(nums) - s):
            j = i + s
            m[i][j], M[i][j] = min_max(i, j, m, M, ops)
    
    
    return M[0][-1]




if __name__ == "__main__":
    print(maximum_value(input()))