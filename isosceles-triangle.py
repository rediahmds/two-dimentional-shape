print(15*'+', 'SEGITIGA SAMA KAKI', 15*'+')
print(8*'+', 'FOR LOOP', 8*'+')
# var to limit the iteration
batas = int(input('Berapa kali loop? '))
count = 1
for space in range(batas, 0, -1):
    print(space*' ' + count*'*')
    count += 2

print()
print()

print(8*'+', 'WHILE LOOP', 8*'+')
# var to count the iteration
count = 1
starMultiplier = 1
# set the space initial value equals to the limit of iteration  
space = batas
while count <= batas:
    print(space*' ' + starMultiplier*'*')
    space -= 1
    count += 1
    starMultiplier += 2