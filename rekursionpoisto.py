result = {}

def count_sequences(n):
    if n == 0:
        return 1
    if n in result:
        return result[n]
    count = 0
    for i in range(2, n + 1, 2):
        count += count_sequences(i - 2) * count_sequences(n - i)
    result[n] = count
    return count


def count_sequences(n):
    # result-taulukkoon tallennetaan välitulokset kaikista eri n:n arvoista
    result = [0] * (n + 1)
    result[0] = 1

    # Luupataan kaikkien tasalukujen läpi
    for i in range(2, n + 1, 2):
        count = 0
        # Laskee tämän hetkisen tasaluvun n:n arvon aiemmin laskettujen tuloksien avulla jotka on 
        # resulttaulukossa
        for x in range(2, i + 1, 2):
            count += result[x - 2] * result[i - x]
        result[i] = count

    return result[n]

print(count_sequences(100))
print(count_sequences_iterative(100))