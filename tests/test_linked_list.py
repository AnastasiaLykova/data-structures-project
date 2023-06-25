import unittest
from src.linked_list import LinkedList, Node


class TestNode(unittest.TestCase):
    def test_init(self):
        n1 = Node(5, None)
        self.assertEqual(n1.next_node, None)
        self.assertEqual(n1.data, 5)


class TestLinkedList(unittest.TestCase):
    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.next_node, None)

    def test_insert_at_end(self):
        ll_2 = LinkedList()
        ll_2.insert_at_end({'id': 2})
        self.assertEqual(ll_2.tail.data, {'id': 2})
        ll_2.insert_at_end({'id': 3})
        self.assertEqual(ll_2.tail.data, {'id': 3})
        self.assertEqual(ll_2.tail.next_node, None)

    def test_str(self):
        ll_3 = LinkedList()
        self.assertEqual(str(ll_3), 'None')
        ll_3.insert_beginning({'id': 1})
        ll_3.insert_at_end({'id': 2})
        ll_3.insert_at_end({'id': 3})
        ll_3.insert_beginning({'id': 0})
        self.assertEqual(str(ll_3), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")
