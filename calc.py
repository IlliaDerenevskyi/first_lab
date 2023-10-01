while True:
    a = float(input("число..."))
    b = float(input("число..."))
    c = input("дія...")
    d = a+b
    f = a-b
    v = a*b
    e = a/b
    if c == "+":
        print(d)
    elif c == "-":
        print(f)
    elif c == "*":
        print(v)
    elif c == "/":
        if b == "0":
            print("Error...")
        else:
            print(e)