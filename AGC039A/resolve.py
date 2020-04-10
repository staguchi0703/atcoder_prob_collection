def resolve():
    '''
    code here
    Sを先頭　真ん中　お尻の三分割する
    連結した場合を考えると以下の場合分け
    先頭　お尻　真ん中×K　（先頭₊お尻）×（K-1）
    同じ文字が続いたらn//2個の文字変更が必要
    以上で解けるはず

    '''
    line = input()
    K = int(input())


    base_cnt = 0
    prev = line[0]
    
 = (base_cnt +1) * (K - 1) + 


    
    print(res)

if __name__ == "__main__":
    resolve()
