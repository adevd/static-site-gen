import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_no_value(self):
        leaf = LeafNode("p", None)
        self.assertRaises(ValueError, leaf.to_html)
        
    def test_to_html(self):
        paragraph_leaf = LeafNode("p", "This is a paragraph of text.")
        link_leaf = LeafNode("a", "Click Me!",  {"href": "adevd.com/linko_friendo"})
        expected_paragraph_result = '<p>This is a paragraph of text.</p>'
        expected_link_result = '<a href="adevd.com/linko_friendo">Click Me!</a>'
        self.assertEqual(paragraph_leaf.to_html(), expected_paragraph_result)
        self.assertEqual(link_leaf.to_html(), expected_link_result)
