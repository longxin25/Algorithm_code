

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    # 查找指定节点
    def Search(self, value):
        current = self.root
        while current:
            # 查找到对应值
            if current.value == value:
                return current
            # 当前节点值小于待查找节点，尝试搜索右子树
            elif current.value < value:
                current = current.right
            # 搜索左子树
            else:
                current = current.left
        return None

    # 插入节点
    def Insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        current = self.root
        while current:
            # 当前节点值小于待插入节点，尝试向右子树插入
            if current.value < value:
                if not current.right:
                    current.right = TreeNode(value)
                else:
                    current = current.right
            if current.value > value:
                if not current.left:
                    current.left = TreeNode(value)
                else:
                    current = current.left

    # 删除节点
    def Delete(self, value):
        current = self.root
        prev = None
        # 查找节点
        while current:
            if current.value == value:
                break
            if current.value < value:
                prev = current
                current = current.right
            if current.value > value:
                prev = current
                current = current.left
        # 没找到
        if not current:
            return
        # TODO: 补全代码
        