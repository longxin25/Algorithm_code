from graphviz import Digraph
from random import sample
import uuid


class BinaryTree:

    def __init__(self, value=None, left=None, right=None) -> None:
        self.data = value
        self.left = left
        self.right = right
        # self.dot = Digraph(comment='Binary Tree')

    # 前序遍历顺序：根节点->左子树->右子树
    def preorder(self):
        if self.data is not None:
            print(self.data, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    # 中序遍历顺序：左子树->根节点->右子树
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        if self.data is not None:
            print(self.data, end=' ')
        if self.right is not None:
            self.right.inorder()

    # 后序遍历顺序：左子树->右子树->根节点
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.data is not None:
            print(self.data, end=' ')

    # 求树高
    def height(self):
        if self.data is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    # 广度优先遍历（层序遍历）
    def BFS(self):
        if self.data is None:
            return
        MyQueue = []
        MyQueue.append(self)
        while MyQueue:
            BTree_node = MyQueue.pop(0)
            print(BTree_node.data, end=' ')
            if BTree_node.left is not None:
                MyQueue.append(BTree_node.left)
            if BTree_node.right is not None:
                MyQueue.append(BTree_node.right)

    '''
    # 利用Graphviz实现二叉树的可视化
    def print_tree(self, save_path='./Binary_Tree.gv', label=False):

        # colors for labels of nodes
        colors = ['skyblue', 'tomato', 'orange', 'purple', 'green', 'yellow', 'pink', 'red']

        # 绘制以某个节点为根节点的二叉树
        def print_node(node, node_tag):
            # 节点颜色
            color = sample(colors,1)[0]
            if node.left is not None:
                left_tag = str(uuid.uuid1())            # 左节点的数据
                self.dot.node(left_tag, str(node.left.data), style='filled', color=color)    # 左节点
                label_string = 'L' if label else ''    # 是否在连接线上写上标签，表明为左子树
                self.dot.edge(node_tag, left_tag, label=label_string)   # 左节点与其父节点的连线
                print_node(node.left, left_tag)

            if node.right is not None:
                right_tag = str(uuid.uuid1())
                self.dot.node(right_tag, str(node.right.data), style='filled', color=color)
                label_string = 'R' if label else ''  # 是否在连接线上写上标签，表明为右子树
                self.dot.edge(node_tag, right_tag, label=label_string)
                print_node(node.right, right_tag)

        # 如果树非空
        if self.data is not None:
            root_tag = str(uuid.uuid1())                # 根节点标签
            self.dot.node(root_tag, str(self.data), style='filled', color=sample(colors,1)[0])     # 创建根节点
            print_node(self, root_tag)

        self.dot.render(save_path)                              # 保存文件为指定文件
    '''

    
if __name__ == '__main__':
    # 构造二叉树, BOTTOM-UP METHOD
    right_tree = BinaryTree(6)
    right_tree.left = BinaryTree(2)
    right_tree.right = BinaryTree(4)

    left_tree = BinaryTree(5)
    left_tree.left = BinaryTree(1)
    left_tree.right = BinaryTree(3)

    tree = BinaryTree(11)
    tree.left = left_tree
    tree.right = right_tree

    left_tree = BinaryTree(7)
    left_tree.left = BinaryTree(3)
    left_tree.right = BinaryTree(4)

    right_tree = tree # 增加新的变量
    tree = BinaryTree(18)
    tree.left = left_tree
    tree.right = right_tree

    print('先序遍历为:')
    tree.preorder()
    print()

    print('中序遍历为:')
    tree.inorder()
    print()

    print('后序遍历为:')
    tree.postorder()
    print()

    print('层序遍历为:')
    tree.BFS()
    print()
    # 利用Graphviz进行二叉树的可视化
    # tree.print_tree(save_path='./create_btree_by_list.gv', label=True)