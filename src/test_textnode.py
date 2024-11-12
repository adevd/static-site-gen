import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertTrue(node.__eq__(node2))

    def test_ineq(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.LINK)
        self.assertFalse(node.__eq__(node2))
        self.assertNotEqual(node2, node3)

    def test_repr(self):
        node = TextNode("Yes", TextType.LINK, "eyo.com")
        self.assertEqual(node.__repr__(), "TextNode(Yes, link, eyo.com)")

    def test_default_link(self):
        node = TextNode("", TextType.IMAGE)
        self.assertIsNone(node.url)
if __name__ == "__main__":
    unittest.main()
