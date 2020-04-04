# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os

file_path = __file__.rsplit('/',1)[0]
f=open(file_path + '/input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可

def resolve():
    '''
    code here
    '''
    N = int(input())
    trans_list = [int(input()) for _ in range(N)]

    memo = [0 for _ in range(6)]
    memo[0] = N


    def trans(i, num):
        if memo[i] > num:
            memo[i] -= num
            memo[i+1] += num
        else:
            memo[i+1] += memo[i]
            memo[i] = 0
            


    res = 0
    while memo[5] != N:
        for i in reversed(range(5)):
            print(i, trans_list[i])
            if memo[i] > 0:
                trans(i, trans_list[i])
        res += 1
        print(memo)
    print(res)

if __name__ == "__main__":
    resolve()
