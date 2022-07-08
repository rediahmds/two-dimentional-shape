print(15*'+', 'SEGITIGA SIKU SIKU GANJIL', 15*'*')
print(8*'+', 'FOR LOOP', 8*'*')
# define how much the iteration occur
batas = int(input('Berapa kali loop? '))

# define the loop with the step +2 in order to get odd number
for i in range(1, batas + 1, 2):
    print(i*'*')

print()
print()

print(8*'+', 'WHILE LOOP', 8*'*')
# declare a dummy var as multiplier
count = 1
while count <= batas:
    if count % 2 == 1:
        print(count*'*')
    count += 1
