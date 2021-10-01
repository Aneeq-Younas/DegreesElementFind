def cont(n):
    result = True
    x, y, z = 5, 7, 3

    while result:

        if str(y) in n:
            z += 1
            y = pow(x, z)

        else:
            result = False

        return z - 1;

print(cont("63635335"))
print(cont("834798568934"))
