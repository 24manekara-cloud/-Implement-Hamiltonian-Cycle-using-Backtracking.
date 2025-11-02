n = 5
x = [0] * (n + 1)
G = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 1, 0, 1, 1, 0]
]


def next_vertex(k):
    global n, x, G
    while True:
        x[k] = (x[k] + 1) % (n + 1)
        if x[k] == 0:
            return
        if G[x[k - 1]][x[k]] != 0:
            j = 1
            while j < k and x[j] != x[k]:
                j += 1
            if j == k:
                if (k < n) or (k == n and G[x[n]][x[1]] != 0):
                    return


def hamiltonian(k):
    global n, x, G
    while True:
        next_vertex(k)
        if x[k] == 0:
            return
        if k == n:
            print(x[1:n+1])
        else:
            hamiltonian(k + 1)


x[1] = 1
print("Hamiltonian Cycles:-")
hamiltonian(2)
