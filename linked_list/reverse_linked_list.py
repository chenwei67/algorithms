class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head: Node):
    """
    不变量：
        r: 反转后的链表头结点
        head: 剩余待反转的链表的结点
    """
    if not head:
        return None
    r = head
    head = head.next
    r.next = None
    while head:
        next_node = head.next
        head.next = r
        r = head
        head = next_node
    return r
