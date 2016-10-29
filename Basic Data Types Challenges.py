# Find the Second Largest Number
n = int(input())
num = map(int, input().split())
print (sorted(list(set(num)))[-2])          #set function turns unique number
        

# Nested Lists        
n = int(input())
l = []
for _ in range(n):
    name = input()
    grade = float(input())
    l.append([name, grade])     #generate list

secondhi = sorted(list(set([marks for name, marks in l])))[1]       #list comprehension -- only select marks for marks and names
print('\n'.join([a for a, b in sorted(l) if b == secondhi]))

#Finding the percentage
n = int(input())
dic = {}
for _ in range(n):
    info = [i for i in input().split()]
    marks = list(map(float, info[1:]))
    dic[info[0]] = sum(marks)/len(marks)

print('{0:.2f}'.format(dic[input()]))
