while True:
    button = input("enter 'a' or 'b'")

    if button == "a" or button == "A" or button == "а" or button == "А":

        a = input("enter some text...")
        b = input("enter one letter for overkill")

        c = a.count(b)
        print("letter", b,"in", a, "=", c)
    elif button == "b" or button == "B" or button == "б" or button == "Б":

        g = str(input("text="))

        list1 = g.split()
        list2 = []
        
        for i in range(len(list1)):
            if len(list[i]) > 3: 
                if list1[i] in list2:
                    i = i+1
                else:
                    if list1[i][-1] == ",":
                        list1[i] = list1[i][:-1]
                        list2.append(list1[i])
                        i = i+1
            for j in range(len(list2)):
                print(list2[j])
                j += 1