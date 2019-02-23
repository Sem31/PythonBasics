# pass by reference



def change(list1):
    print("id in function : ",id(list1)) # id is same as before calling and after calling

    list1[2] = 30
    print("list is : ",list1)
    return

list1 = [1,2,3,4,5]
print("id outside the function : ",id(list1))# id is same as before calling and after calling
change(list1)
print("out side the function after the change list : ",list1)



def newchange(list2):
    list2 = [1,2,3,4,5]
    print("inside function new list id is : ",id(list2))
    list2[2] = 20
    print("after the change is : ",list2)

list2= [10,20,40,50,60]
print("outside function list id is : ",id(list2))
print("list2 is  : ",list2)
newchange(list2)

