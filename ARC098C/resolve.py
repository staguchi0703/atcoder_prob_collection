def resolve():
    '''
    code here
    '''
    N = int(input())
    S = input()

    W_list = [0 for _ in range(N)]
    E_list = [0 for _ in range(N)]
    
    for i, s in enumerate(S):
        if i == 0:
            if s == 'W':
                W_list[i] = 1
        else:
            W_list[i] = W_list[i-1]
            if s == 'W':
                W_list[i] += 1

        
    for i, s in enumerate(S[::-1]):
        if i == 0:
            if s == 'E':
                E_list[i] = 1
        else:
            E_list[i] = E_list[i-1]
            if s == 'E':
                E_list[i] += 1
    
    E_list = E_list[::-1]

    sum_list = []
    for i in range(N):
        sum_list.append(E_list[i] + W_list[i])

    res = min(sum_list) -1
    print(res)


if __name__ == "__main__":
    resolve()
