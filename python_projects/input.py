# num=input()
# print("you entered ", num)

# try:
  #  num = int(input("Enter a number: "))
  #  print("you entered" , num)
  #  num+=1
# except:
  #  print("You did not enter a number")

with open('movies.txt') as file:
    for line in file:
        print(line.strip(), end=' ') # print defaults making new line, this gets rid of it I think

name = "Bob"
print("Hello, my friend", name)
print(f'Hello, my friend {name}')
hello = f'Hello, my friend {name}'
print(hello)

with open('heights.txt') as file:
    for line in file:
        line=line.strip()
        print(line)
        values=line.split() #split breaks up into substrings separated by the whitespaces
        print(values)