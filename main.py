import random

from avl_skeleton import AVLNode, AVLTreeList

b = AVLTreeList();

b.insert(0,"1")
b.insert(0,"2")
b.insert(0,"3")
b.insert(0,"4")
b.insert(0,"succ parent")
b.insert(0,"delete")
b.insert(0,"7")
b.insert(0,"8")
b.insert(0,"9")
b.insert(4,"succ")
b.display()
print(b.listToArray())
b.delete(3)
b.display()
print(b.listToArray())

# b.display()
b.listToArray()
deletions=0
insertions=0
for i in range(1,100000):
    arr=b.listToArray()
    if len(arr)==1: print(arr)
    action=random.randint(0,1)
    # print("pre-action:******************************************")
    # print("length is: ", b.length())
    # print("tree looks like: ")
    # b.display()
    if b.length()-1==0:
        action=0
        index=0
    else: index = random.randrange(0, min(i,b.length()-1))
    if action==0:
        # print("list form before insertion : ", b.listToArray())
        # print("about to insert ",i," in index: ", index)
        size = b.length()
        b.insert(index, str(i))
        if (size - b.length() != -1):
            print("WTFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
            break
        insertions+=1
        # print("tree after insertion :")
        # print("list form: ", b.listToArray())
    else:
        # print("list form before deletion : ", b.listToArray())
        # print("about to delete ", b.retrieve(index), " in index: ", index)
        size=b.length()
        b.delete(index)
        if(size-b.length()!=0 and size-b.length()!=1):
            print("WTFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
            break
        deletions=deletions+1
        #
        # print("tree after deletion :")
        # print("list form: ", b.listToArray())

b.display()
print("sucess!!!!!!")
print("list form: ", b.listToArray())
print("length is: ", b.length())
print(deletions, "deletions")
print(insertions, "deletions")
print(insertions+deletions)