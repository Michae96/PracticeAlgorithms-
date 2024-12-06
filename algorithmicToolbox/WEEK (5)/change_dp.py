import sys


def change(money):

    
    min_coins = [0] * (money+1)
    for m in range(1, money+1):
        min_coins[m] = sys.maxsize
        for coin in [1, 3, 4]:
            
            
            if m >= coin:
                
                
                num_coins = min_coins[m - coin] + 1
                if num_coins < min_coins[m]:
                    min_coins[m] = num_coins
    
    return min_coins[-1]


if __name__ == '__main__':
    m = int(input())
    print(change(m))