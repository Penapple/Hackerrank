#Upper to lower, lower to upper case
st = input()
print(''.join(i.upper() if i.islower() else i.lower() for i in st)) #'i for i in st' is object. Both join([]) and join(i for i in x) work

#Strings Validators
S = input()
print([s for s in S if s.isupper()])        #character in list; for before if
print(any(s.isupper() for s in S))      #Amazing built-in function any

#Text alignment
print(input().ljust(25, '-')    #or use rjust, center
      
#String Formatting
n = int(input())
width = len('{0:b}'.format(n))      #pyformat.info
for i in range(1, n+1):
    print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
      
#Alphabet Rangoli
import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))
      
#Capitalize
s = input()
l = []
c = [c for c in s]
c[0] = c[0].upper()
for i in range(len(c)):
    if c[i-1] == ' ':
        c[i] = c[i].upper()
print(''.join(c))

#Capitalize -- easy way
s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())    #Capitalize the word in s but not change the structure of s (including space)
print(s)
      
#Merge the Tools
s, n = input(), int(input())
#sorted(x, key=x.index) to order; set() to make it unique
for i in range(int(len(s)/n)):
    se = [x for x in s[i*n:(i+1)*n]]
    print(''.join(sorted(set(se), key=se.index)))
