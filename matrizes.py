rows = int(input("Linhas: "))
columns = input().strip().split(", ")
matriz = [[*columns] for _ in range(rows)]
print(*matriz, sep="\n")