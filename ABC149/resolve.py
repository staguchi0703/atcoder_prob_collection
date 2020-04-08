def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    R, S, P= [int(item) for item in input().split()]
    T = input()
    memo = [1 for _ in range(K)]
    def point_chk(s):
        if s == 'r':
            return P
        elif s == 's':
            return R
        elif s == 'p':
            return S
        else:
            raise

    
    max_point = 0
    for i, s in enumerate(T):
        if i < K:
            max_point += point_chk(s)
            memo[i%K] = s
        else:
            if s == memo[i%K]:
                memo[i%K] = 1
            else:
                memo[i%K] = s
                max_point += point_chk(s)
        # print(i, s, memo, max_point)
    
    print(max_point)

if __name__ == "__main__":
    resolve()
