class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None

        result = self.head.data
        self.head = self.head.next_node
        return result

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        temp_list = []
        temp_obj = self.head
        while temp_obj is not None:
            temp_list.append(temp_obj.data)
            temp_obj = temp_obj.next_node
        return "\n".join(temp_list)
