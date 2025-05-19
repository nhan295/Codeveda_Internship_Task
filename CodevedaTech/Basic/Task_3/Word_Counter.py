

with open("text.txt",'r') as f:
    content = f.read()

print(content)

arr = content.split()
count = 0
for i in arr:
    count+=1

print(' Total word in file: '+ str(count))


