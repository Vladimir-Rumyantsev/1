def knapsack(N, Z, weights, values):
    K = [[0 for i in range(Z+1)] for i in range(N+1)]

    for i in range(N+1):
        for w in range(Z+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i - 1] +                # Ценность текущего элемента
                              K[i - 1][w - weights[i - 1]],  # Ценность предыдущих элементов в рюкзаке
                              K[i - 1][w])                   # Ценность, если не брать
            else:
                K[i][w] = K[i-1][w]

    result = []
    w = Z
    for i in range(N, 0, -1):
        if K[i][w] != K[i-1][w]:                            # Если да, значит мы брали новый предмет
            result.append(i)
            w -= weights[i-1]

    result.reverse()
    return result, K[N][Z]


with open('input.txt', 'r') as file:
    N, Z = map(int, file.readline().split())
    weights = list(map(int, file.readline().split()))
    values = list(map(int, file.readline().split()))

result, max_value = knapsack(N, Z, weights, values)
print("Подмножество артефактов:", result)
print("Суммарный вес:", sum(weights[i-1] for i in result))
print("Общая ценность:", max_value)
