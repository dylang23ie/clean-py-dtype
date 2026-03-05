ls = [1,2,3]

print("multiple list",ls*3)

square_ls=[]

for x in ls:
    square_ls.append(x**2)

    print("Squared:", square_ls)

    cubed_ls = [x**3 for x in ls]

    print("cubed:", cubed_ls)