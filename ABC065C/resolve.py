def resolve():
    '''
    code here

    '''
    import math

    N, M = [int(item) for item in input().split()]

    deff = N - M

    if deff == -1:
        N, M = M, N

    if deff == 0:
        res = (math.factorial(N)**2 * 2) % (10**9+7)

    elif abs(deff) == 1:
        res = (math.factorial(N) **2 // N ) % (10**9+7)

    else:
        res = 0
    
    print(res)

if __name__ == "__main__":
    resolve()
