'''
This file implements the Binary Search Tree data structure.
The functions in this file are considerably harder than the functions in the
BinaryTree file.
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    The BST is a superclass of BinaryTree.
    That means that the BST class "inherits" all of the methods from
    BinaryTree, and we don't have to reimplement them.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''
        super().__init__()
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be
        used to recreate a valid instance of the class.
        Thus, if you create a variable using the command BST([1,2,3])
        it's __repr__ will return "BST([1,2,3])"

        For the BST, type(self).__name__ will be the string "BST",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of BST will have a
        correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete
        functions are actually working.

        FIXME:
        Implement this function.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        ret = True
        if node.left:
            if node.value >= node.left.value:
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= node.right.value:
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        '''
        Inserts value into the BST.

        FIXME:
        Implement this function.

        HINT:
        Create a staticmethod helper function following the pattern of
        _is_bst_satisfied.
        '''
        if self.root:
            return BST._insert(value, self.root)

        self.root = Node(value)

    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if node.left is not None:
                BST._insert(value, node.left)
            else:
                node.left = Node(value)

        elif value > node.value:
            if node.right is not None:
                BST._insert(value, node.right)
            else:
                node.right = Node(value)

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.

        HINT:
        Repeatedly call the insert method.
        You cannot get this method to work correctly until you have gotten
        insert to work correctly.
        '''
        for x in xs:
            self.insert(x)

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.

        FIXME:
        Implement this function.
        '''
        if self.root:
            return BST._find(value, self.root)
        return False

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = False
        if (value < node.value) & (node.left is not None):
            return BST._find(value, node.left)
        elif (value > node.value) & (node.right is not None):
            return BST._find(value, node.right)
        elif value == node.value:
            ret = True
        return ret

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.

        HINT:
        Create a recursive staticmethod helper function,
        similar to how the insert and find functions have recursive helpers.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.

        FIXME:
        Implement this function.

        HINT:
        Create a recursive staticmethod helper function.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        '''
        Removes value from the BST.
        If value is not in the BST, it does nothing.

        FIXME:
        Implement this function.

        HINT:
        You must have find_smallest/find_largest working correctly
        before you can implement this function.

        HINT:
        Use a recursive helper function.
        if self.root:
            BST._remove(value, self.root)
        '''
        if self.root:
            if self.root.value == value:
                if self.root.left is not None:
                    self.root.value = BST._find_largest(self.root.left)
                    self.root.left = BST._remove(self.root.value,
                                                 self.root.left)
                elif self.root.right is not None:
                    self.root.value = BST._find_smallest(self.root.right)
                    self.root.right = BST._remove(self.root.value,
                                                  self.root.right)
                else:
                    self.root = None
            else:
                BST._remove(value, self.root)

    @staticmethod
    def _remove(value, node):
        if (value < node.value) and (node.left is not None):
            node.left = BST._remove(value, node.left)
            return node
        elif (value > node.value) and (node.right is not None):
            node.right = BST._remove(value, node.right)
            return node
        elif value == node.value:
            if node.left is not None:
                node.value = BST._find_largest(node.left)
                node.left = BST._remove(node.value, node.left)
                return node

            elif node.right is not None:
                node.value = BST._find_smallest(node.right)
                node.right = BST._remove(node.value, node.right)
                return node

            else:
                return None
        else:
            return node

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.

        FIXME:
        Implement this function.
        '''
        for x in xs:
            self.remove(x)
