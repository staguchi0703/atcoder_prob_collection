
def resolve():
    '''
    code here
    x=一発で通る時間
    y=全てのテストケースが通る時間
    x = 1900M + 100(N-M)
    y = x + (1 - (1/2)**M )y :::ここで失敗してから終わる時間の期待値は終わる時間の期待値そのもの
    →変形すると　y = 2**M x
    よって　y = (1900M + 100(N-M)) * 2 ** M  
    '''
    N, M = [int(item) for item in input().split()]

    print((1900 * M + 100 * (N - M)) * 2 ** M)

if __name__ == "__main__":
    resolve()
