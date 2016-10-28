# Find the Second Largest Number
n = int(input())
num = map(int, input().split())
print (sorted(list(set(num)))[-2])          #set function turns unique number
        
