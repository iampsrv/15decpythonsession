while(1):
    try:
        x= int(input("Enter the value of x"))
        y= int(input("Enter the value of y"))
        a=x/y
        print(f"The value of a is {a}")
    except ZeroDivisionError as e:
        print("Dont give the value of y zero")
    else:
        print("no exception occured")
    finally:
        print("finally block executed")