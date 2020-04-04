
def resolve():
    '''
    code here
    '''
    N = int(input())
    trans_list = [int(input()) for _ in range(5)]

    memo = [0 for _ in range(6)]
    memo[0] = N


    def trans(i, num):
        if memo[i] > num:
            memo[i] -= num
            memo[i+1] += num
        else:
            memo[i+1] += memo[i]
            memo[i] = 0
            


    res = 0
    while memo[5] != N:
        for i in reversed(range(5)):
            # print(i, trans_list[i])
            if memo[i] > 0:
                trans(i, trans_list[i])
        res += 1
        # print(memo)
    print(res)

if __name__ == "__main__":
    resolve()
