#multiple no in function( we can pass any no. of parameters in python by using the * key)


def sum(*li):
    print(li)


li = [1,2,3,4]
sum(li)