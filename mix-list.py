a = input("word:")
b = int(input("к-сть ключів:"))
 

list1 = ""

list2 = ""
list3 = ""
list4 = ""

if b == 2:
    for i in range(0, len(a), 2):
        list1 += a[i]
    for i in range(1, len(a), 2):
        list2 += a[i]
    print(list1)
    print(list2)
    print(list1+list2)
elif b == 3:
    for i in range(0, len(a), 2):
        list1 += a[i]
    for i in range(1, len(a), 2):
        list2 += a[i]
    for i in range(1, len(a), 3):
        list3 += a[i]
        list1 = list1.replace(a[i], "")
        list2 = list2.replace(a[i], "")
    print(list1)
    print(list2)
    print(list3+a[-1])
    print(list1+list2+list3+a[-1])

elif b == 4:
    for i in range(0, len(a), 2):
        list1 += a[i]
    for i in range(1, len(a), 2):
        list2 += a[i]
    for i in range(1, len(a), 3):
        list3 += a[i]
        list1 = list1.replace(a[i], "")
        list2 = list2.replace(a[i], "")
    for i in range(1, len(a), 4):
        list4 += a[i]
        list1 = list1.replace(a[i], "")
        list2 = list2.replace(a[i], "")
        list3 = list3.replace(a[i], "")
    print(list1)
    print(list2)
    print(list3)
    print(list4)

