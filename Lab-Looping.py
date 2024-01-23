num1 = int(input("enter an integer "))
equal = "=" * 6
print(f"number\tsquared\tcubed\n{equal}\t{equal}\t{equal}")

for x in range(num1):
    print(f"{x+1}\t\t{(x+1) ** 2}\t\t{(x+1) ** 3}")

    x += 1

print()
print(f'{1}\t{2}\t{3}\t{4}\n_\t_\t_\t_')

for x in range(num1):
    print(f'{x+1}|\t{((x+1) * 1)}\t{(x+1) * 2}\t{(x+1) * 3}\t{(x+1) * 4}')
    x += 1


