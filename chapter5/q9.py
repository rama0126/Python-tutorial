#myargv.py   for Q9 
import sys
result = 0
a = sys.argv[1:]
for i in a:
    result += int(i)
print(result)