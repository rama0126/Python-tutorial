f = open('test_for_Q7.txt','r')
body = f.read()
f.close()

body = body.replace("java","python")

f = open('test_for_Q7.txt','w')
f.write(body)
f.close()