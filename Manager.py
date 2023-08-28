def Remove(name, list):
    if name in list:
        list.remove(name)
        print(name,"has been removed correctly!")
    else:
        print("You gave the wrong data!")

def Search(name,list):
    if name in list:
        print(name,"is on the list!")
    else:
        print(name," is not on the list!!!")