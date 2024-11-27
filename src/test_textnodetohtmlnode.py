import unittest
from textnodetohtmlnode import text_node_to_html_node
from textnode import TextType, TextNode
"""
def text_node_to_html_node(text_node):
Copy icon
It should handle each type of the TextType enum. If it gets a TextNode that is none of those types, it should raise an exception.

TextType.TEXT: This should become a LeafNode with no tag, just a raw text value.
TextType.BOLD: This should become a LeafNode with a "b" tag and the text
TextType.ITALIC: "i" tag, text
TextType.CODE: "code" tag, text
TextType.LINK: "a" tag, anchor text, and "href" prop
TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
"""


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_to_html_invalid_inputs(self):
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node("I'm a string of text")
        self.assertEqual(str(context.exception), "Invalid argument: requires a TextNode")
    
    def test_texttoleafnode(self):
        text_node = TextNode("this is the text", TextType.TEXT)
        result = text_node_to_html_node(text_node)
        self.assertEqual(result.value, "this is the text")
        self.assertEqual(result.tag, None)

    def test_bold_to_leaf_node(self):
        text_node = TextNode("Bold text!", TextType.BOLD)
        result = text_node_to_html_node(text_node)
        self.assertEqual(result.value, "Bold text!")
        self.assertEqual(result.tag, "b")

    def test_italic_to_leaf_node(self):
        text_node = TextNode("Italic text!", TextType.ITALIC)
        result = text_node_to_html_node(text_node)
        self.assertEqual(result.value, "Italic text!")
        self.assertEqual(result.tag, "i")








