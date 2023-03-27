def vectorization(num):
    i = 2
    fact = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            fact.append(i)
    if num > 1:
        fact.append(num)
    print(fact)
    return fact

vectorization(12)