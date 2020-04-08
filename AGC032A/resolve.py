def resolve():
    '''
    code here
    考え方がポイントの問題
    aの先頭からj番目にjを挿入する
    →先頭からj番目の数字がjのときにjの最大値を列から削除する

    '''
    import collections
    
    N = int(input())
    b_list = [int(item) for item in input().split()]
    a = collections.deque()

    is_True = True

    while is_True:
        stack = collections.deque()
        for i in range(len(b_list)):
            if i+1 == b_list[i]:
                # print(b_list[i])
                stack.append(b_list[i])
                # print(stack)
        if len(stack) == 0:
            is_True = False
            a = [-1]
        else:
            temp = stack.pop()
            a.append(temp)
            del b_list[temp-1]
            # print(b_list)

        if len(b_list) == 0:
            is_True = False

    for i in reversed(a):
        print(i)
if __name__ == "__main__":
    resolve()
