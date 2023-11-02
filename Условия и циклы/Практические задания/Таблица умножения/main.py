size = 9
# for i in range(2, size+1):
#     for j in range(2, size+1):
#         result = i * j
#         end = " " if j != size else ""
#         print(f'{result:2}', end=end)
#     print()

# for i in range(2, size + 1):
#     output = ""
#     for j in range(2, size + 1):
#         result = i * j
#         output += f"{result:2} "
#     print(output[:-1])

for i in range(2, size + 1):
    for j in range(2, size + 1):
        result = i * j
        if j != size:
            znak = " "
        else:
            znak = ""
        print(f"{result:2}", end=znak)
    print("")