def my_Function():
    for num in range(1, 255): # (start, stop, iterate/step)
        print(num)
my_Function()


myList = [1, 2, 3]
myList.append(5) #adding 5 to end of list; .append is a method
print(myList)

print(len(myList)) #length of my list

#anatomy of a python function
def myFunction (parameter):
    for num in range(101, 2, -5): #range is a function
        print(num)

def num_1_to_10(): #defines fucntion
    for i in range(1,11):
        print(i)
        if i%2 ==1:
            print("this is odd")
        elif i%2 ==0:
            print("this is even")

num_1_to_10() #calls function here to work

def multiply(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
[2,4,10,16]

