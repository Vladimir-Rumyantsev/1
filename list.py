class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self) -> str:
        current = self.head
        line = ''
        while current:
            line = f'{line}, {str(current)}'
            current = current.next
        return f'[{line[2:]}]'

    def __len__(self) -> int:
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def add(self, data, index=-1):
        if index < 0:
            index += len(self) + 1
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        if (self.head is None) or (index < 0):
            raise IndexError("Индекс выходит за пределы списка")
        current = self.head
        for i in range(index - 1):
            current = current.next
            if current is None:
                raise IndexError("Индекс выходит за пределы списка")
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def pop(self, index=-1):
        if index < 0:
            index += len(self)
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        if (self.head is None) or (index < 0):
            raise IndexError("Индекс выходит за пределы списка")
        current = self.head
        for i in range(index - 1):
            current = current.next
            if current is None:
                raise IndexError("Индекс выходит за пределы списка")
        data = current.next.data
        current.next = current.next.next
        return data


stack = LinkedList()
print(f'\nStack: {stack}\nlen: {len(stack)}')

stack.add(1)
print(f'\nStack: {stack}\nlen: {len(stack)}')

stack.add(2)
print(f'\nStack: {stack}\nlen: {len(stack)}')

stack.add(3)
print(f'\nStack: {stack}\nlen: {len(stack)}')

stack.pop()
print(f'\nStack: {stack}\nlen: {len(stack)}')

amount = 0
for item in stack:
    amount += item
print(f'\nThe amount: {amount}')
