for i in range(1,10):
    print(i)
print(i)

for k in range(1,10):
    print(k,end='')
print()
for k in range(1,10):
    print(k,' ',end='')
print()

# formatting the output of print()
# using 5 spaces, and justify to the right

for j in range(1000,1050,5):
    print('{0:5d}'.format(j))

for a in range(1,101):
    print('{0:3d}'.format(a))

# nested for - loops

for row in range(1,10):
    for col in range(1,5):
        print(row,col,'  ',end='')
    print()