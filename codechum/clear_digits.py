# Write a script that will remove the non-digit base on the left side of the digit

user = input("Input: ")
x = list(user)
empty = []
ans = []
#Added len(x)-1 so that j+1 wont exceed to the index, because range stop at certain the given range, so adding 
for j in range(len(x)-1):
    if x[j+1].isnumeric():
        empty.append(x[j])
        empty.append(x[j+1])
        
    if x[j] not in empty:
        ans.append(x[j])

print(''.join(ans))


'''
3 = [1,2,3]  = len(x)

0
1
2 = if nag j[0+1] it will be j[1] = 2
new loop = j[1+1] = j[2] = 3
new loop = j[2+1] = j[3] = OUT OF INDEX


so we add -1 in the range:

3 = [1,2,3] = len(x)- 1:
0
1
first loop = j[0+1] = j[1] = 2
new loop = j[1+1] = j[2] = 3


SEE TO NOT BE OUT OF INDEX YOU NEED -1
'''