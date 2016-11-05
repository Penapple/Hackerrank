#Upper to lower, lower to upper case
st = input()
print(''.join(i.upper() if i.islower() else i.lower() for i in st)) #'i for i in st' is object. Both join([]) and join(i for i in x) work
