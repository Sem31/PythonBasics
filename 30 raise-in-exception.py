# raise exception

try:
    marks = int(input("enter the markse :"))
    if marks<0 or marks>100:
        raise Exception(marks)
    print("marks is valid range : ",marks)
except Exception as e:
    print("error...",e)
