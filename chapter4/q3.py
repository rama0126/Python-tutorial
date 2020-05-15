#Before
input1 = input("input first number : ")
input2 = input("input second number : ")

total = input1 + input2
print(" Sum of numbers is {0} ".format(total)) #total = 36 , have to be 9

#After
input1 = input("input first number : ")
input2 = input("input second number : ")
input1 = int(input1)
input2 = int(input2)
total = input1 + input2
print(" Sum of numbers is {0} ".format(total)) #total = 9