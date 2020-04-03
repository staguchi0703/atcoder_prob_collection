def resolve():
    '''
    code here
    '''
    N = int(input())
    cards = [int(item) for item in input().split()]

    all_sum = sum(cards)

    
    def candi_abs(sumu):
        # print(sumu, all_sum - sumu, abs(2*sumu - all_sum))
        return abs(2*sumu - all_sum)

    res = 3 * 10**9
    sumu = 0
    for i in range(N-1):
        sumu += cards[i] 
        res = min(res, candi_abs(sumu))

    print(res)


if __name__ == "__main__":
    resolve()
