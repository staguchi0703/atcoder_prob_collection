def resolve():
    '''
    code here
    '''
    from decimal import Decimal
    a, b, c = [int(item) for item in input().split()]
    
    x = c - a - b
    y = 2 * Decimal(a*b).sqrt()

    if y < x:
        print('Yes')
    else:
        print('No')




if __name__ == "__main__":
    resolve()
