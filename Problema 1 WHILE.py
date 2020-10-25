"""Se introduc succesiv numere nenule până la introducerea numărului 0. Să se afişeze suma tuturor numerelor introduse."""
n=eval(input("introducati un numar:"))
s=0
while n!=0:
    s+=n
    n=eval(input("introduceti un numar:"))

print("suma numerelor introduse este:",s)