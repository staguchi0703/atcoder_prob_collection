def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    R, S, P= [int(item) for item in input().split()]
    T = input()
    path_num = min(K, N-K)
    memo = [1 for _ in range(path_num)]
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
            memo[i%path_num] = s
        else:
            if s != T[i-K]:
                max_point += point_chk(s)
                memo[i%path_num] = s
            else:
                temp = memo[(i-1)%path_num]
                if temp == s:
                    memo[i%path_num] = s
                else:
                    memo[i%path_num] = s
                    max_point += point_chk(s)

        print(i, s, memo, max_point)
    
    print(max_point)

if __name__ == "__main__":
    resolve()
