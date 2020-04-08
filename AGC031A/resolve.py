def resolve():
    '''
    code here
    各文字について、個数+1（使わない）の選択肢がある
    全ての場合は選択肢の個数の積である
    全て使わないも含まれてしまうので-1する
    pow(10,p)+7で割った余りを答える
    '''
    import sys
    N = int(input())
    S = sys.stdin.readline().strip()
    mod = pow(10, 9) + 7
    set_S = set([item for item in S])
    res = 1

    for s in set_S:
        cnt = 1
        for letter in S:
            if s == letter:
                cnt += 1
        res *= cnt
        res %= mod

    mod = pow(10, 9) + 7
    print(res-1)

if __name__ == "__main__":
    resolve()
