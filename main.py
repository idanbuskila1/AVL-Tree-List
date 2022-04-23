import random
import sys

import numpy as np
import matplotlib.pyplot as plt

from avl_skeleton import AVLNode, AVLTreeList
from BSTList import BSTList


def main():
    q_3()


def q_3():
    sys.setrecursionlimit(1000000)
    MAX_I = 10
    rebalancing_ops_mean = {'avl_first': [], 'avl_balanced': [], 'avl_random': [],
                            'bst_first': [], 'bst_balanced': [], 'bst_random': []}
    insertion_depth_mean = {'avl_first': [], 'avl_balanced': [], 'avl_random': [],
                            'bst_first': [], 'bst_balanced': [], 'bst_random': []}

    for i in range(1, MAX_I+1):
        avl_first = AVLTreeList()
        avl_balanced = AVLTreeList()
        avl_random = AVLTreeList()
        bst_first = BSTList()
        bst_balanced = BSTList()
        bst_random = BSTList()
        n = i * 1000

        rebalancing_ops_and_insertion_depth_i = {'avl_first': [], 'avl_balanced': [], 'avl_random': [],
                                                 'bst_first': [], 'bst_balanced': [], 'bst_random': []}

        ### first ###
        for j in range(n):
            rebalancing_ops_and_insertion_depth_i['avl_first'].append(avl_first.insert(0, str(j), depthStats=True))
            rebalancing_ops_and_insertion_depth_i['bst_first'].append(bst_first.insert(0, str(j), depthStats=True))

        ### balanced ###
        # insertion indices;
        # 0
        # 0,2
        # 0,2,4,6
        # 0,2,4,6,8,10,12,14 etc.
        count = 0
        max_ = 2
        rebalancing_ops_and_insertion_depth_i['avl_balanced'].append(avl_balanced.insert(0, str(count), depthStats=True))
        rebalancing_ops_and_insertion_depth_i['bst_balanced'].append(bst_balanced.insert(0, str(count), depthStats=True))
        count += 1
        while avl_balanced.length() < n:
            for j in range(0, max_ + 2, 2):
                rebalancing_ops_and_insertion_depth_i['avl_balanced'].append(avl_balanced.insert(j, str(count), depthStats=True))
                rebalancing_ops_and_insertion_depth_i['bst_balanced'].append(bst_balanced.insert(j, str(count), depthStats=True))
                count += 1
            max_ *= 2
            max_ += 2

        ### random ###
        for j in range(n):
            if avl_random.length() != 0:
                index = random.randint(0, avl_random.length()-1)
            else:
                index = 0
            rebalancing_ops_and_insertion_depth_i['avl_random'].append(avl_random.insert(index, str(j), depthStats=True))
            rebalancing_ops_and_insertion_depth_i['bst_random'].append(bst_random.insert(index, str(j), depthStats=True))

        for key in rebalancing_ops_mean.keys():
            rebalancing_ops_mean[key].append(np.mean([x[0] for x in rebalancing_ops_and_insertion_depth_i[key]]))
            insertion_depth_mean[key].append(np.mean([x[1] for x in rebalancing_ops_and_insertion_depth_i[key]]))

    x = np.arange(1, MAX_I+1, 1)
    fig = plt.figure(1)
    for key, data_list in rebalancing_ops_mean.items():
        plt.plot(x, data_list, label=key)
    plt.xticks(x)
    plt.xlabel('tree size = 1000 * i')
    plt.grid(axis='y')
    plt.title('q.3 mean number of rebalancing operations')
    plt.legend()
    fig.show()

    fig = plt.figure(2)
    for key, data_list in insertion_depth_mean.items():
        plt.plot(x, data_list, label=key)
    plt.xticks(x)
    plt.xlabel('tree size = 1000 * i')
    plt.grid(axis='y')
    plt.title('q.3 mean of the inserted node depth')
    plt.legend()
    fig.show()

    with open('q3_rebalancing_ops_means.txt', 'w') as f:
        for key in rebalancing_ops_mean.keys():
            f.write(key + '\n')
            for i in range(0, MAX_I):
                f.write(str(rebalancing_ops_mean[key][i]) + '\n')

    with open('q3_insertion_depth_means.txt', 'w') as f:
        for key in rebalancing_ops_mean.keys():
            f.write(key + '\n')
            for i in range(0, MAX_I):
                f.write(str(insertion_depth_mean[key][i]) + '\n')

    plt.show()



def q_2():
    results = {'average join cost for random split': [],
               'maximum join cost for random split': [],
               'average join cost for last in left subtree split': [],
               'maximum join cost for last in left subtree split': []}
    POW = 11
    for i in range(1, POW):
        a = AVLTreeList()
        b = AVLTreeList()
        n = pow(2, i) * 1000
        for j in range(n):
            if a.length() != 0:
                index = random.randint(0, a.length()-1)
            else:
                index = 0
            a.insert(index, str(j))
            b.insert(index, str(j))

        # random split
        index = random.randint(0, a.length()-1)
        joins = a.split(index, joinStats=True)[3]
        results['average join cost for random split'].append(np.mean(joins))
        results['maximum join cost for random split'].append(0 if len(joins) == 0 else np.max(joins))

        # last in left sub-tree split
        joins = b.split(b.getRoot().getLeft().getSize()-1, joinStats=True)[3]
        results['average join cost for last in left subtree split'].append(np.mean(joins))
        results['maximum join cost for last in left subtree split'].append(0 if len(joins) == 0 else np.max(joins))

    x = np.arange(1, POW, 1)
    fig = plt.figure(1)
    for key, data_list in results.items():
        plt.plot(x, data_list, label=key)
    plt.xticks(x)
    plt.xlabel('tree size = 1000 * 2^i')
    plt.grid(axis='y')
    plt.title('q.2')
    plt.legend()
    fig.show()

    fig = plt.figure(2)
    for key in ('average join cost for last in left subtree split', 'average join cost for random split'):
        plt.plot(x, results[key], label=key)
    plt.xticks(x)
    plt.xlabel('tree size = 1000 * 2^i')
    plt.grid(axis='y')
    plt.title('q.2')
    plt.legend()
    fig.show()

    with open('q2.txt', 'w') as f:
        for key in ('maximum join cost for last in left subtree split',
                    'average join cost for last in left subtree split',
                    'maximum join cost for random split',
                    'average join cost for random split'):
            f.write(key + '\n')
            for i in range(0, POW-1):
                f.write(str(results[key][i]) + '\n')


    # print("round ", "#", " :", 'maximum join cost for last in left subtree split', " :",
    #       'average join cost for last in left subtree split', " :",
    #       'maximum join cost for random split', " :",
    #       'average join cost for random split')
    # for i in range(0, POW-1):
    #     print("round ", i, " :", results['maximum join cost for last in left subtree split'][i], " :",
    #           results['average join cost for last in left subtree split'][i], " :",
    #           results['maximum join cost for random split'][i], " :",
    #           results['average join cost for random split'][i])

    plt.show()







def q_1():
    b = AVLTreeList()
    for i in range(1,11):
        n=pow(2,i)*1000
        changes=0
        for j in range(n//2):
            if b.length()!=0:
                index = random.randrange(0,b.length())
            else: index=0
            b.insert(index,str(i))
        for k in range(n//4):
            index=random.randrange(0,b.length())
            changes+= b.delete(index)
            index = random.randrange(0, b.length())
            changes += b.insert(index, str(i))
        print("round ",i," :",changes)
    #
    # b.insert(0,"1")
    # b.insert(0,"2")
    # b.insert(0,"3")
    # b.insert(0,"4")
    # b.insert(0,"succ parent")
    # b.insert(0,"delete")
    # b.insert(0,"7")
    # b.insert(0,"8")
    # b.insert(0,"9")
    # b.insert(4,"succ")
    # b.display()
    # print(b.listToArray())
    # b.delete(3)
    # b.display()
    # print(b.listToArray())
    #
    # # b.display()
    # b.listToArray()
    # deletions=0
    # insertions=0
    # for i in range(1,100000):
    #     arr=b.listToArray()
    #     if len(arr)==1: print(arr)
    #     action=random.randint(0,1)
    #     # print("pre-action:******************************************")
    #     # print("length is: ", b.length())
    #     # print("tree looks like: ")
    #     # b.display()
    #     if b.length()-1==0:
    #         action=0
    #         index=0
    #     else: index = random.randrange(0, min(i,b.length()-1))
    #     if action==0:
    #         # print("list form before insertion : ", b.listToArray())
    #         # print("about to insert ",i," in index: ", index)
    #         size = b.length()
    #         b.insert(index, str(i))
    #         if (size - b.length() != -1):
    #             print("WTFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    #             break
    #         insertions+=1
    #         # print("tree after insertion :")
    #         # print("list form: ", b.listToArray())
    #     else:
    #         # print("list form before deletion : ", b.listToArray())
    #         # print("about to delete ", b.retrieve(index), " in index: ", index)
    #         size=b.length()
    #         b.delete(index)
    #         if(size-b.length()!=0 and size-b.length()!=1):
    #             print("WTFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    #             break
    #         deletions=deletions+1
    #         #
    #         # print("tree after deletion :")
    #         # print("list form: ", b.listToArray())
    #
    # b.display()
    # print("sucess!!!!!!")
    # print("list form: ", b.listToArray())
    # print("length is: ", b.length())
    # print(deletions, "deletions")
    # print(insertions, "deletions")
    # print(insertions+deletions)


def split_test():
    i = 8
    T = AVLTreeList()
    count = 0
    for j in range(20):
        T.append(count)
        count += 1
        T.insert(j//2, count)
        count += 1
    print(T.listToArray())
    print(T.length())
    print('splitting by ' + str(i))
    res = T.split(i)
    print('left')
    print(res[0].listToArray())
    res[0].display()
    print('right')
    print(res[2].listToArray())
    res[2].display()
    print()


def balanced_insert_demo():
    MAX_I = 2
    for i in range(1, MAX_I):

        avl_balanced = AVLTreeList()
        n = i * 10
        count = 0
        max = 2

        print('### [0] ###')
        print('insert(' + str(0) + ',' + str(count) + ')')
        avl_balanced.insert(0, str(count))
        count += 1
        avl_balanced.display()
        print()

        while avl_balanced.length() < n:

            print('### [' + ','.join([str(i) for i in range(0, max + 2, 2)]) + '] ###')
            for j in range(0, max + 2, 2):
                print('insert(' + str(j) + ',' + str(count) + ')')
                avl_balanced.insert(j, str(count))
                avl_balanced.display()
                print()
                count += 1
            max *= 2
            max += 2
        avl_balanced.display()




if __name__ == '__main__':
    main()
