a = input("word:")
b = int(input("к-сть ключів:"))

list1 = []
list2 = []
list3 = []
list4 = []
if b == 2:
    for i in range(0, len(a), 2):
        list1 += a[i]
    for i in range(1, len(a), 2):
        list2 += a[i]
    print(list2)
    print(list1)
    b2 = list1 + list2
    print(b2)
elif b == 3:
    for i in range(0, len(a), 4):
        list1 += a[i]
    for i in range(1, len(a), 2):
        list2 += a[i]
    for i in range(2, len(a), 4):
        list3 += a[i]
    print(list3)
    print(list2)
    print(list1)
    b3 = list3 + list2 + list1
    print(b3)
elif b == 4:
    for i in range(0, len(a), 5):
        list1 += a[i]
    for i in range(1, len(a), 3):
        list2 += a[i]
    for i in range(2, len(a), 4):
        list3 += a[i]
    for i in range(3, len(a), 5):
        list4 += a[i]
    print(list4)
    print(list3)
    print(list2)
    print(list1)
    b4 = list4 + list3 + list2 + list1
    print(b4)
    
