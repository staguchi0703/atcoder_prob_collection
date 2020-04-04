
def resolve():
    '''
    code here
    '''
    import math
    N = int(input())
    trans_list = [int(input()) for _ in range(5)]

    min_tp = min(trans_list)
    
    print(math.ceil(N/min_tp) + 4)

if __name__ == "__main__":
    resolve()
