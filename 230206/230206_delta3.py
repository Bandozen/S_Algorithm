di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
P = 3
for i in range(N):
    for j in range(N):
        for k in range(4):
            for l in range(1, P+1):
                ni = i + di[k] * l
                nj = j + dj[k] * l
                if 0 <= ni < N and 0 <= nj < N:
                    print(i, j, ni, nj)