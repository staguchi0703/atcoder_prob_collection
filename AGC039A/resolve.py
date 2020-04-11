def resolve():
    '''
    code here
    Sを先頭　真ん中　お尻の三分割する
    連結した場合を考えると以下の場合分け
    先頭　お尻　真ん中×K　（先頭₊お尻）×（K-1）
    同じ文字が続いたらn//2個の文字変更が必要
    以上で解けるた

    '''
    S = input()
    K = int(input())

    S_head = ''
    head = S[0]
    for s in S:
        if s == head:
            S_head += s
        else:
            break
    
    S_tail = ''
    tail = S[-1]
    for s in S[::-1]:
        if s == tail:
            S_tail += s
        else:
            break
    S_tail = S_tail[::-1]

    S_body = S[len(S_head):-1 * len(S_tail)]
    
    def double_counter(S):
        cnt = 0
        if len(S) >= 2:
            prev = S[0]
            for item in S[1:]:
                if item == prev:
                    cnt += 1
                    prev = -1
                else:
                    prev = item

        return cnt
    
    if len(S) >= 2 and len(S) != len(S_head):
        res = len(S_head)//2\
            + len(S_tail)//2\
            + double_counter(S_body) * K\
            + double_counter(S_tail+S_head) * (K-1)
    elif len(S) == 1:
        res = K // 2
    elif len(S) == len(S_head):
        res = (K * len(S)) // 2

    print(res)

if __name__ == "__main__":
    resolve()
