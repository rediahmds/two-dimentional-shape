print(15*'+', 'SEGITIGA SIKU SIKU', 15*'*')
print(8*'+', 'FOR LOOP', 8*'*')

# define how much the iteration occur
batas = int(input('Berapa kali loop? '))
for i in range(1, batas + 1):
    print(i*'*')

# give some space in between
print()
print()

count = 1
print(8*'+', 'WHILE LOOP', 8*'*')
while count <= batas:
    print(count*'*')
    count += 1
