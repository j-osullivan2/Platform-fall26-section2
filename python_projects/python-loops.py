for i in range(1, 21):

    if(i%3==0):
        print(i)

counter = 1
total = 0
while counter < 51:
    if (counter%2==0):
        total += counter
    counter+=1
print (total)

lst = [5,8,2,15,10,3,7]

for i in range(len(lst)):
    if (lst[i]>5):
        print(lst[i])

st=[0,3,8,4,5]

def swap(lst):
    temp = lst[0]
    lst[0]= lst[len(lst)-1]
    lst[len(lst)-1]=temp

swap(st)
print(st[len(st)-1])

