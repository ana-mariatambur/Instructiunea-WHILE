"""Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. Să se afişeze suma tuturor numerelor pare introduse.  """
n=eval(input("introduceti un sir de numere:"))
s=0

while n%2==0 or (n%2!=0 and n%3!=0):
    if n%2==0:
        s+=n

    n=eval(input("introduceti un sir de numere:"))

print("suma numerelor pare introduse este:",s) 