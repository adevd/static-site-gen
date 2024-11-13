import unittest

from htmlnode import HTMLNode, HTMLNodeType

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        test_node = HTMLNode(HTMLNodeType.LINK.value, None , None, {"href": "adevd.com"})
        self.assertEqual(test_node.__repr__(), "HTMLNode(tag: a, value: None, children: None, props: {\'href\': \'adevd.com\'})")

    def test_props_to_html(self):
        test_node = HTMLNode(None, None, None, {"alt": "cool image of friends", "src": "adevd.com/cool_image.png"})
        self.assertEqual(test_node.props_to_html(), " alt=\"cool image of friends\" src=\"adevd.com/cool_image.png\" ")


if __name__ == '__main__':
    unittest.main()
