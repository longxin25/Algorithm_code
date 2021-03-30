

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
        # 要删除的节点有两个子节点
        if current.left and current.right:
            # 记录该节点的右子树和右子树的父节点
            temp = current.right
            temp_parent = current
            # 向左搜索直到找到最小节点
            while temp.left:
                temp_parent = temp
                temp = temp.left
            # 最小节点替换至要删除节点位置
            current.value = temp.value
            # 删除最小节点 TODO:确认代码正确
            prev, current = temp_parent, temp
            return
        # 要删除的节点有零或一的子节点
        if current.left:
            child = current.left
        else:
            child = current.right
        # 要删除的节点是根节点
        if not prev:
            # 直接用子节点替换掉根节点
            self.root = child
        # 要删除的节点是左子树
        elif prev.left == current:
            # 此节点的父节点左指针指向此节点的孩子节点
            prev.left = child
        else:
            prev.right = child
