user_input = input("input what you wnat to save : ")
f = open('test.txt','a')
f.write(user_input)
f.write("\n")
f.close()