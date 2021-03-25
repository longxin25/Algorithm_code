

class BinaryTree:

    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    # 前序遍历顺序：根节点->左子树->右子树
    def preorder(self):
        if self.value is not None:
            print(self.value, end='')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    # 中序遍历顺序：左子树->根节点->右子树
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        if self.value is not None:
            print(self.value, end='')
        if self.right is not None:
            self.right.inorder()

    # 后序遍历顺序：左子树->右子树->根节点
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.value is not None:
            print(self.value, end='')

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

    