def resolve():
    '''
    code here
    '''
    import sys
    sys.setrecursionlimit(10000000)
    from decimal import Decimal
    N = int(input())
    T_list = [int(input()) for _ in range(N)]

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a%b)

    def lcm(a,b):
        return a // gcd(a, b) * b # /するとfloatになり桁が足りなくてエラーになる
        # intのままで計算すればint64で計算できる

    res = 1
    for i in T_list:
        res = lcm(res, i)
        # print(res, i)

    print(res)

if __name__ == "__main__":
    resolve()
