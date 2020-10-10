from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        curr = self.head
        str1 = ""
        while curr:
            str1 += f"{curr} --> "
            curr = curr.next
        return str1 + "END"

    def get(self, index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def insert(self, index, data):  # 插入
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise IndexError("下标越界")
        elif self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.get(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def remove(self, index):  # 删除
        temp = self.head
        if index < 0 or index >= self.size:
            raise IndexError("下标越界")
        elif self.size == 0:
            raise IndexError("链表为空,无需删除")
        elif index == 0:
            self.head = temp.next
            remove_node = temp
            temp.next = None
        elif index == self.size - 1:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = prev.next.next
        self.size -= 1
        return remove_node

    def reverse(self):  # 反转
        prev = None
        curr = self.head
        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
        self.head = prev

    def linklist(self, obj: List):  # 链表插入
        self.head = Node(obj[0])
        temp = self.head
        for i in obj[1:]:
            temp.next = Node(i)
            temp = temp.next

    def __setitem__(self, index, data):
        if self.head is None:
            raise IndexError("链表为空,无法更改")
        else:
            curr = self.get(index)
            curr.data = data
        return curr

    def set(self, index, data):
        return self.__setitem__(index, data)


ll = LinkList()
ll.insert(0, 1)
ll.insert(1, 1)
ll.insert(2, 2)
ll.insert(2, 3)
ll.insert(1, 100)
print(f"原链表为: {ll}\n原链表大小为: {ll.size}")
ll.remove(0)
print(f"删除头部: {ll}\n删除头部链表大小为: {ll.size}\n")
print(f"原链表为: {ll}\n原链表大小为: {ll.size}")
ll.remove(3)
print(f"删除尾部: {ll}\n删除尾部链表大小为: {ll.size}\n")
print(f"原链表为: {ll}\n原链表大小为: {ll.size}")
ll.remove(1)
print(f"删除中间: {ll}\n删除中间链表大小为: {ll.size}\n")
print(f"原链表为: {ll}")
ll.reverse()
print(f"反转链表为: {ll}")
ll.linklist(list(range(1, 7)))
print(f"{ll}\n")
print(f"原链表为: {ll}")
index = 3
print(
    f"改变结点的位置为: {index}, 对应的节点为: {ll.get(index)}, 改变后结点为: {ll.set(index, 300)}")
print(f"改变后链表为: {ll}")
