def resolve():
    '''
    code here
    '''
    line = input()

    cnt = 1
    prev = line[0]

    if len(line) == 1:
        res = 0
    else:
        for item in line[1:]:
            if item == prev:
                pass
            else:
                cnt += 1
            prev = item
        res = cnt -1
    print(res)

if __name__ == "__main__":
    resolve()
