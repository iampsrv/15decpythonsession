square = []
for a in range(10):
    if a % 2 !=0:
        square.append(a**2)
# print(square)

new_square_list = [a**2 for a in range(10) if a % 2 !=0]
print(new_square_list)