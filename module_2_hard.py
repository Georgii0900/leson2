def shifr (n):
    passw = ""
    for i in range(1, n):

        for j in range(i, n):
            if i == j:
                continue

            if n % (i+j) == 0:
                passw += f"{i}{j}"
    return passw


print(shifr(5))

