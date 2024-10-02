principal = 900000
rate = 0.085
numyears= 20
year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    print(f"{year:>3d} {principal:0.2f}")
    year += 1

print(15//4)
