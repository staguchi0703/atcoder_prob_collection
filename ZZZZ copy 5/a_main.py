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
            a = -1
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

