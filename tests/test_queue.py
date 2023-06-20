import unittest
from src.queue import Node, Queue


class TestNode(unittest.TestCase):

    def test_init(self):
        n1 = Node(5, None)
        self.assertEqual(n1.next_node, None)
        self.assertEqual(n1.data, 5)


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node, None)
        queue.enqueue('data2')
        self.assertEqual(queue.tail.data, 'data2')
        self.assertEqual(queue.head.next_node.data, 'data2')

    def test_str(self):
        queue_2 = Queue()
        queue_2.enqueue('data1')
        queue_2.enqueue('data2')
        self.assertEqual(str(queue_2), 'data1\ndata2')

    def test_dequeue(self):
        queue_3 = Queue()
        queue_3.enqueue('data1')
        self.assertEqual(queue_3.dequeue(), 'data1')
        self.assertEqual(queue_3.dequeue(), None)
