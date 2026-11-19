print("hello world!")

# Comment yo

x = 100
print(x)

x = 5.5
print(x)

x = [1, 2, 3]
print(x)

x = 100 
y = 10
z = x/y

print(z)

z= int(z)
print(z)

result = x//y
print (result)

min_val = min(10,2)
print(min_val)
raised = pow(2,4)
print(raised)
raised=2**4
print(raised)

if x<0:
    print("x is less tha 0")
print("next line") # one line indentation

if x<0 and y<0:
    print ("both less than 0")

if x<0 or y<0:
    print("at least one of them is less than 0")

if x<0:
    print("less than 0")
elif x>0:
    print("greater than 0")
else:
    print (0)
    
counter = 0
while counter < 10:

     print (counter)
     counter += 1

for i in range (5):
        print (i)

for i in range (2,5):

            print(i)

lst = [1, 2,3,4,5]

for i in range (len(lst)):
            print(i,lst[i])

# functions with a parameter 
def hello(name):

    print("Hello",name)

hello("Rob")

full_name = "The Akron Hammer"
first_Name=full_name[:3]
middle_name=full_name[4:9]
last_name=full_name[10:]
first_inital=full_name[0]
last_inital=full_name[15]

print (middle_name)