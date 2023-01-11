# level 2
name = input("Enter name ")
i = 0
for x in name:
    if x == "n":
        print("\nThe character 'n' present at index no ,", i, "value = ", x)
        break
    print(x, end=" ")
    i += 1


# level 1
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)
#
#     # print: 1 2 3 4