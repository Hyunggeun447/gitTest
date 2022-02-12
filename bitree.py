class Node:
    def __init__(self, value):
        # double linked list
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head  # 루트노드

    # 삽입
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:  # 이미 가지고 있다면
                    self.current_node = self.current_node.left  # 비교대상을 바꾼다.
                else:
                    self.current_node.left = Node(value)  # 없다면 새로 만들어 연결시킨다.
                    break
            else:
                if self.current_node.right != None:  # 이미 가지고 있다면
                    self.current_node = self.current_node.right  # 비교대상을 바꾼다.
                else:
                    self.current_node.right = Node(value)
                    break

    # 이진 탐색 트리 출력
    def search(self, value):
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == value:  # 찾았다
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left  # 비교대상 바꾸기
            else:
                self.current_node = self.current_node.right  # 비교대상 바꾸기
        return False  # 다 찾아봤는데 없다.

# 실행
head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)

print(BST.search(2))
print(BST.search(5))

print(list(BST))