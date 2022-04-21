# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.
@type value: str
@param value: data of your node
"""

    def __init__(self, value, height=0, size=1):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = height
        self.size = size


    """returns the left child
@rtype: AVLNode
@returns: the left child of self, None if there is no left child
"""

    def getLeft(self):
            return self.left

    """returns the right child
@rtype: AVLNode
@returns: the right child of self, None if there is no right child
"""

    def getRight(self):
        return self.right

    """returns the parent 
@rtype: AVLNode
@returns: the parent of self, None if there is no parent
"""

    def getParent(self):
        return self.parent

    """return the value
@rtype: str
@returns: the value of self, None if the node is virtual
"""

    def getValue(self):
        return self.value

    """returns the height
@rtype: int
@returns: the height of self, -1 if the node is virtual
"""

    def getHeight(self):
        return self.height

    """returns the size
   @rtype: int
   @returns: the size of self, 0 if the node is virtual
   """

    def getSize(self):
        return self.size

    """sets left child
@type node: AVLNode
@param node: a node
"""

    def setLeft(self, node):
        self.left = node

    """sets right child
@type node: AVLNode
@param node: a node
"""

    def setRight(self, node):
        self.right = node

    """sets parent
@type node: AVLNode
@param node: a node
@param isLeft: boolean value that indicates if self is node's left or right child.
"""

    def setParent(self, node):
        self.parent=node
    """
       update child as the right child of self.
       @param child: avl node. to be the right child of self.
        """
    def makeRightChild(self, child):
        self.setRight(child)
        if child.isRealNode():
            child.setParent(self)

    """
       update child as the left child of self.
       @param child: avl node. to be the left child of self.
        """
    def makeLeftChild(self, child):
        self.setLeft(child)
        if child.isRealNode():
            child.setParent(self)
    """
    changing all pointers of given node to None.
    """
    def garbage(self):
        self.left=None
        self.right=None
        self.parent=None
    """
calculates ballance factor of given node
"""
    def getBF(self):
        return self.getLeft().getHeight()-self.getRight().getHeight()

    """sets value
@type value: str
@param value: data
"""
    def setValue(self, value):
        self.value = value

    """sets the balance factor of the node
@type h: int
@param h: the height
"""

    def setHeight(self, h):
       self.height =h

    """sets the size of the node
@type h: int
@param h: the size
"""

    def setSize(self, s):
        self.size = s

    """returns whether self is not a virtual node 
@rtype: bool
@returns: False if self is a virtual node, True otherwise.
"""

    def isRealNode(self):
        return False if self.height == -1 else True

"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    virtualNode = AVLNode(None, -1, 0)  # class attribute for the sentinel object

    """
Constructor, you are allowed to add more fields.
"""
    def __init__(self):
        self.root = None


    def display(self):
        def printTree(node, level=0):
            if node is not self.virtualNode:
                printTree(node.getRight(), level + 1)
                print(' ' * 4 * level + '-> ' + str(node.getValue()))
                printTree(node.getLeft(), level + 1)
        if self.empty():
            print("empty tree")
        else:
            printTree(self.root)
    """returns whether the list is empty
    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """
    def empty(self):
        return True if self.root is None else False

    """checks if given node is leaf
    @parm node: node to check
    @rtype: boolean
    @returns: true if node is leaf, false otherwise
    """
    def isLeaf(self, node):
        if node.getRight() is self.virtualNode and node.getLeft() is self.virtualNode:
            return True
        return False
    """retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""

    def retrieve(self, i):
        return self.treeSelect(i+1).getValue()

    """finds and returns the node with rank i in tree
           @pre: 0 <= i < self.length()
           @param i: the rank of desired node
           @type i: int
           @returns: rank i node
           """

    def treeSelect(self, i):

        def treeSelectRec(x, k):
            r = x.getLeft().getSize() + 1
            if k == r:
                return x
            elif k < r:
                return treeSelectRec(x.getLeft(), k)
            else:
                return treeSelectRec(x.getRight(), k - r)

        return treeSelectRec(self.root, i)

    """performs right rotation for AVL balancing
       @param node: the highest node of the three nodes involved in right rotation
       """

    def rightRotation(self, node):
        # pointers set up
        left_node = node.getLeft()
        parent=node.getParent()
        sub_tree = left_node.getRight()
        # rotate
        left_node.makeRightChild(node)
        node.makeLeftChild(sub_tree)
        if parent is None: #we have rotated the root
           self.root=left_node
           left_node.setParent(None)
        elif parent.getLeft() is node:
            parent.makeLeftChild(left_node)
        else: parent.makeRightChild(left_node)

    """performs left rotation for AVL balancing
        @param node: the highest node of the three nodes involved in left rotation
        """
    def leftRotation(self, node):
        # pointers set up
        right_node = node.getRight()
        parent = node.getParent()
        sub_tree=right_node.getLeft()
        # rotate
        right_node.makeLeftChild(node)
        node.makeRightChild(sub_tree)
        if parent is None: #we have rotated the root
            self.root = right_node
            right_node.setParent(None)
        elif parent.getRight() is node:
            parent.makeRightChild(right_node)
        else: parent.makeLeftChild(right_node)

    """updates height and size of every node in a given list in order
        @parm nodes: list of AVL nodes
        @rtype: int
        @returns: 1 if node height was changed not as part of rotation, 0 otherwise
    """
    def update(self, nodes):
        for node in nodes:
            node.setSize(1 + node.getLeft().getSize() + node.getRight().getSize()) #update size
            #update height if needed:
            calc_height=1 + max(node.getLeft().getHeight(), node.getRight().getHeight())
            if calc_height != node.getHeight():#there is height conflict after insertion/deletion
                node.setHeight(calc_height)
                if len(nodes) == 1:  # height of single node was changed, not as part of rotation
                    return 1
        return 0

    """ballances the path between y to root by AVL rules and updates size & height
            @param node: the node to begin the check with
            @type node: AVL_Node
            @returns: number of rotations and height updates made in process
        """

    def fixTree(self, y):
        changes=0
        while y is not None:
            height_changed = self.update([y])#correct size and height, variable stores 1 if height was changed
            #correct ballance:
            BF = y.getBF()
            if BF==2:
                if y.getLeft().getBF()==-1:
                    self.leftRotation(y.getLeft())
                    self.rightRotation(y)
                    changes = changes + 2
                    self.update([y, y.getParent().getLeft(), y.getParent()])
                else:# left BF is +1 or 0
                    self.rightRotation(y)
                    changes = changes + 1
                    self.update([y, y.getParent()])
                y = y.getParent()
            elif BF==-2:
                if y.getRight().getBF() == 1:
                    self.rightRotation(y.getRight())
                    self.leftRotation(y)
                    changes = changes + 2
                    self.update([y, y.getParent().getRight(), y.getParent()])
                else:# right BF is -1 or 0
                    self.leftRotation(y)
                    changes = changes + 1
                    self.update([y, y.getParent()])
                y = y.getParent()
            else: #no rotations made for y
                if height_changed: changes +=1 #if height changed without rotation, add 1 change to count
            y=y.getParent()
        return changes

    """inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def insert(self, i, val):
        n = self.length()
        inserted=None
        assert 0 <= i <= n
        if n == 0: #empty tree
            self.root = AVLNode(val)
            inserted=self.root
        elif i == n: #insert last
            inserted= self.insertLast(val)
        else: #0<=i<n
            node=self.treeSelect(i+1)
            if node.getLeft() is self.virtualNode:#make it his left child
                node.makeLeftChild(AVLNode(val))
                inserted=node.getLeft()
            else:#left once than all the way right
                node = node.getLeft()
                while node.getRight() is not self.virtualNode:
                    node = node.getRight()
                node.makeRightChild(AVLNode(val))
                inserted=node.getRight()
        inserted.setRight(self.virtualNode)
        inserted.setLeft(self.virtualNode)
        return 0 if inserted is self.root else self.fixTree(inserted.getParent())

    """inserts node at the last position
            @pre: self.empty() == False
            @param val: value of the new node
            @type val: string
            @returns: pointer to the inserted node
            @rtype: AVL Node
            """
    def insertLast(self, val):
        node = self.root
        while node.getRight() is not self.virtualNode:
            node = node.getRight()
        node.makeRightChild(AVLNode(val))
        return node.getRight()


    """
    deletes node, given its a leaf in the tree
    @param node: node to delete
    @pre: node is leaf
    @param parent: parent of node
"""
    def deleteLeaf(self, node, parent):
        if parent is None:#the root is leaf - we create an empty tree
            self.root=None
        elif parent.getLeft() is node:
            parent.makeLeftChild(self.virtualNode)
        else: parent.makeRightChild(self.virtualNode)
    """
    deletes a node given it has only one child
    @param node: node to delete
    @pre: node has exactly one child
    @param parent: parent of node
"""
    def deleteOneChildNode(self,parent, node):
        child = node.getLeft() if node.getLeft().isRealNode() else node.getRight()
        if parent is None:#we delete the root which has only one child
            self.root=child
            child.setParent(None)
        elif parent.getLeft() is node: parent.makeLeftChild(child)
        else: parent.makeRightChild(child)

    """
    returns pointer to successor of a given node
    @pre: node has right child
    @param node: the node to search successor for
    @rtype: AVL node
    """
    def successor(self, node):
        node=node.getRight()
        while node.getLeft() is not self.virtualNode:
            node = node.getLeft()
        return node


    """deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
    def delete(self, i):
        n = self.length()
        assert 0 <= i < n and n != 0
        node = self.treeSelect(i + 1)
        # case 1: delete a leaf
        if self.isLeaf(node):
            parent=node.getParent()
            self.deleteLeaf(node, parent)
        # case 2: delete a node with 2 children
        elif node.getLeft() is not self.virtualNode and node.getRight() is not self.virtualNode:
           succ=self.successor(node)
           parent=succ.getParent() #parent of successor of node
           #remove successor from tree
           self.deleteLeaf(succ, parent) if self.isLeaf(succ) else self.deleteOneChildNode(parent, succ) #successors never have left child
           #replace node with successor
           succ.makeRightChild(node.getRight())
           succ.makeLeftChild(node.getLeft())
           if node.getParent() is None: #we deleted the root
               self.root=succ
               succ.setParent(None)
           else: #we deleted a regular node
                if node.getParent().getLeft() is node:
                     node.getParent().makeLeftChild(succ)
                else: node.getParent().makeRightChild(succ)
           if parent is node: parent=succ #we start rebalancing from parent, if parent is deleted update to succ
        # case 3: only one child.
        else:
            parent=node.getParent()
            self.deleteOneChildNode(parent, node)
        node.garbage()
        return 0 if parent is None else self.fixTree(parent)

    """returns the value of the first item in the list
	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""

    def first(self):
        if self.root is None: return None
        node=self.root
        while(node.getLeft() is not self.virtualNode):
            node=node.getLeft()
        return node.getValue()

    """returns the value of the last item in the list
	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""

    def last(self):
        if self.root is None: return None
        node = self.root
        while (node.getRight() is not self.virtualNode):
            node = node.getRight()
        return node.getValue()
    """returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""

    def listToArray(self):
        if self.empty():
            return []

        def rec_listToArray(node, lst):
            if node.getLeft() is not self.virtualNode:
                rec_listToArray(node.getLeft(),lst)
            # if abs(node.getBF()) == 2:
            #     print("ballance ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR   ", node.getBF())
            #     return["ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"]
            ret.append(node.getValue())
            if node.getRight() is not self.virtualNode:
                rec_listToArray(node.getRight(), lst)
        ret=[]
        rec_listToArray(self.root, ret)
        return ret

    """returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""

    def length(self):
        if self.root is None:
            return 0
        return self.root.getSize()


    """returns the height of the AVL tree 

    @rtype: int
    @returns: the height of the AVL tree
    """

    def height(self):
        if self.root is None:
            return -1
        return self.root.getHeight()


    """joins self, x, and other 
    @type x: str
    @post: self < x < other (in terms of rank)
    @param x: the value of the node to be ranked between self and other
    @type other: AVLTreeList
    @param other: an AVL tree to be joined with self
    """
    def join(self, x, other):
        if self.empty() and other.empty():
            self.insert(0, x)
        elif self.empty():
            other.insert(0, x)
            self.root = other.getRoot()
        elif other.empty():
            self.insert(self.length(), x)

        elif abs(self.height() - other.height()) <= 1:
            new_root = AVLNode(x)
            new_root.makeLeftChild(self.root)
            new_root.makeRightChild(other.getRoot())
            self.update([new_root])
            self.root = new_root

        elif self.height() < other.height():
            h = self.height()
            nodeB = other.getRoot()
            while nodeB.getHeight() > h:
                nodeB = nodeB.getLeft()
            parent = nodeB.getParent()      # parent.height == h+1/h+2, nodeB.height == h/h-1
            nodeX = AVLNode(x)
            nodeX.makeLeftChild(self.root)
            nodeX.makeRightChild(nodeB)
            parent.makeLeftChild(nodeX)
            self.root = other.getRoot()
            self.fixTree(nodeX)
        else:
            h = other.height()
            nodeB = self.root
            while nodeB.getHeight() > h:
                nodeB = nodeB.getRight()
            parent = nodeB.getParent()
            nodeX = AVLNode(x)
            nodeX.makeLeftChild(nodeB)
            nodeX.makeRightChild(other.getRoot())
            parent.makeRightChild(nodeX)
            self.fixTree(nodeX)


    """splits the list at the i'th index
    
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""

    def split(self, i):
        nodeX = self.treeSelect(i+1)
        val = nodeX.getValue()
        left = AVLTreeList()
        right = AVLTreeList()

        if nodeX.getLeft() is not self.virtualNode:  # to be joined to a left sub-tree after turning left
            left.makeRoot(nodeX.getLeft())

        if nodeX.getRight() is not self.virtualNode:  # to be joined with a right sub-tree after turning right
            right.makeRoot(nodeX.getRight())

        if nodeX != self.root:
            curNode = nodeX
            parent = nodeX.getParent()
            while parent is not None:
                if parent.getLeft() == curNode:            # turned right
                    rightRightTree = AVLTreeList()
                    if parent.getRight() is not self.virtualNode:
                        rightRightTree.makeRoot(parent.getRight())     # the right sub-tree

                    right.join(parent.getValue(), rightRightTree)

                else:                                       # turned left
                    leftRightTree = AVLTreeList()  # to be joined to a left sub-tree after turning left
                    if not left.empty():
                        leftRightTree.makeRoot(left.getRoot())

                    left = AVLTreeList()
                    if parent.getLeft() is not self.virtualNode:
                        left.makeRoot(parent.getLeft())     # the left sub-tree

                    left.join(parent.getValue(), leftRightTree)

                curNode = parent
                parent = curNode.getParent()

        self.root.garbage()     # this tree is destroyed
        self.root = None

        return [left, val, right]


    """concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""

    def concat(self, lst):
        heightDiff = abs(self.height() - lst.height())
        if self.root is None:
            self.root = lst.getRoot()
        elif lst.getRoot() is not None:
            x = self.last()
            self.delete(self.length()-1)
            self.join(x, lst)
        return heightDiff

    """searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""

    def search(self, val):
        # traverse inorder the AVL sub-tree rooted in node
        # return the first rank that contains val in node's sub-tree, -1 if not found.
        def rec_search(node, val, cur_rank):
            if node.getLeft() is not AVLTreeList.virtualNode:
                res = rec_search(node.getLeft(), val, cur_rank)
                if res != -1:
                    return res
            if node.getValue() == val:
                return cur_rank + node.getLeft().getSize()
            if node.getRight() is not AVLTreeList.virtualNode:
                res = rec_search(node.getRight(), val, cur_rank + node.getLeft().getSize() + 1)
                if res != -1:
                    return res
            return -1     # no val in this sub-tree

        return rec_search(self.root, val, 0) if not self.empty() else -1

    """returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""

    def getRoot(self):
        return self.root


    """update root to be new_root

       @param new_root: avl node. to be the new root of self.
    """
    def makeRoot(self, new_root):
        self.root = new_root
        self.root.setParent(None)

