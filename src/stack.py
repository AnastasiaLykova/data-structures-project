class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data, None)

        # if we have a top node this means that the stack isn't empty
        if self.top:

            # based on the PUSH operation instructions
            # the next node must be the current top node
            new_node.next_node = self.top

        # otherwise, we will set the new top node to be the new_node
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        # Special case: if top node is none (if stack is empty)
        # we will return none
        if self.top is None:
            return None

        # otherwise
        result = self.top.data  # the node thats left in the stack
        self.top = self.top.next_node  # self.top is now going to be equal to
        # whatever it's pointing to

        return result
