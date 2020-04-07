def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    R, S, P= [int(item) for item in input().split()]
    T = input()

    max_point = 0
    for s in T:
        if s == 'r':
            max_point += R
        elif s == 's':
            max_point += S
        else:
            max_point += P
    
    path_num = min(N-K, K)
    discreasing = 0
    for i in range(path_num):
        cnt = (N-i)//K + 1

        s = T[i]
        if s == 'r':
            temp_ratio = R
        elif s == 's':
            temp_ratio = S
        else:
            temp_ratio = P
        # print(discreasing)
        discreasing += (cnt - cnt // 2) * temp_ratio

    print(max_point - discreasing)


if __name__ == "__main__":
    resolve()
