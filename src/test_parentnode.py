import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_none_values(self):
        parent_none_children = ParentNode("ul", None)
        with self.assertRaises(ValueError) as context:
            parent_none_children.to_html()
        self.assertEqual(str(context.exception), "ParentNode children member must not be None" )
        
        parent_none_tag = ParentNode(None, [LeafNode("p", "Hey, I'm a leaf!")])
        with self.assertRaises(ValueError) as context:
            parent_none_tag.to_html()
        self.assertEqual(str(context.exception), "ParentNode tag member must not be None")

    def test_nested_elements(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
           ]
        parent = ParentNode("p",children)
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_complex_list(self):
        list_items = [
            ParentNode("li", ["I have some " , LeafNode("b", "bold text!")])
            ]
        list_parent = ParentNode("ul", list_items)
        div_parent = ParentNode("div", ["Here's a list: ", list_parent], {"class": "list-container"})
        expected_html = "<div class=\"list-container\">Here's a list: <ul><li>I have some <b>bold text!</b></li></ul></div>"
        self.assertEqual(div_parent.to_html(), expected_html)

