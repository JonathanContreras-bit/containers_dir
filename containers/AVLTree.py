'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the
BinaryTree and BST files, but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a
        balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return True
        else:
            return (abs(AVLTree._balance_factor(node)) <= 1) and\
                   (AVLTree._is_avl_satisfied(node.left)) and\
                   (AVLTree._is_avl_satisfied(node.right))

    @staticmethod
    def _copy_nodes(node):
        if node:
            cop = Node(node.value, AVLTree._copy_nodes(node.left),
                       AVLTree._copy_nodes(node.right))
        else:
            return None
        return cop

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        swap = AVLTree._copy_nodes(node.right.left)
        newnode = Node(node.right.value)
        newnode.right = AVLTree._copy_nodes(node.right.right)
        newnode.left = AVLTree._copy_nodes(node)
        newnode.left.right = swap
        return newnode

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        swap = AVLTree._copy_nodes(node.left.right)
        newnode = Node(node.left.value)
        newnode.left = AVLTree._copy_nodes(node.left.left)
        newnode.right = AVLTree._copy_nodes(node)
        newnode.right.left = swap
        return newnode

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert
        into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function
        for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        BST.insert(self, value)
        while not self.is_avl_satisfied():
            self.root = AVLTree._rebalance(self.root)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if node is not None:
            bf = AVLTree._balance_factor(node)
            # right rotation: parent and left have positive BF
            if bf > 1:
                # left sub rotation then right rotation: parent+ left-
                if (AVLTree._balance_factor(node.left) < 0):
                    node.left = AVLTree._left_rotate(node.left)
                want = AVLTree._right_rotate(node)
                node.value = want.value
                node.right = want.right
                node.left = want.left

            # left rotation: parent and right have negative BF
            elif bf < -1:
                # right sub rotation then left rotation: parent- right+
                if (AVLTree._balance_factor(node.right) > 0):
                    node.right = AVLTree._right_rotate(node.right)
                want = AVLTree._left_rotate(node)
                node.value = want.value
                node.right = want.right
                node.left = want.left

            # recursive call
            else:
                AVLTree._rebalance(node.left)
                AVLTree._rebalance(node.right)

            return node
