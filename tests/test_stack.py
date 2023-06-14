import unittest
from src.stack import Node, Stack


class TestNode(unittest.TestCase):

    def test_init(self):
        n1 = Node(5, None)
        self.assertEqual(n1.next_node, None)
        self.assertEqual(n1.data, 5)


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(stack.top.next_node, None)

    def test_pop(self):
        stack_2 = Stack()
        stack_2.push('data1')
        data = stack_2.pop()
        self.assertIsNone(stack_2.top)
        self.assertEqual(data, 'data1')
        data = stack_2.pop()
        self.assertIsNone(data)
