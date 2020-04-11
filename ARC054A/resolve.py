def resolve():
    '''
    code here
    '''
    L, X, Y, S, D = [int(item) for item in input().split()]

    delta = [(D+L - S) % L, (S+L -D) %L]
    vel = [X + Y, X -Y]

    if vel[1] >= 0:
        res = delta[0]/vel[0]
    else:
        res = min(delta[0]/vel[0], abs(delta[1]/vel[1]))

    print(res)


if __name__ == "__main__":
    resolve()
