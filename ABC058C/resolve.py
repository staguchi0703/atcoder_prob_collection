def resolve():
    '''
    code here
    全部の文字列のなかから共通する文字を選ぶ　→　辞書で文字列ごとの各文字の出現回数を記録する
    使える文字数＝各文字の出現数最小値
    実装するには辞書で各文字の出現回数を持つことにする
    各文字数の辞書を表現するのに都合がいいのが、collections.Counter()
    辞書の順序をソートするには  sorted()関数が必要
    戻り値を持つので代入する変数が必要
    　　　＊＊＊inplaceするのは .sort()メソッドだがdictには.sort()メソッドがない
    '''

    import collections
    N = int(input())
    S_list = [collections.Counter(input()) for _ in range(N)]

    cnt_dict = S_list[0]

    for line in S_list:
        for item in cnt_dict.keys():
            cnt_dict[item] = min(line[item], cnt_dict[item])
        prev_dict = cnt_dict
        # print(cnt_dict)
    
    cnt_tuple = sorted(cnt_dict.items())
    # print(cnt_tuple)
    res = ''
    for i, v in cnt_tuple:
        if v > 0:
            res += i*v

    print(res)

if __name__ == "__main__":
    resolve()    

