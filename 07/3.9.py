def fuctorial(n):
    if n <= 1:
        return 1
    else:
        return n * fuctorial(n - 1)

print(fuctorial(4))