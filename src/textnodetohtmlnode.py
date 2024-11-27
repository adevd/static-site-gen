from textnode import TextType, TextNode
from leafnode import LeafNode

"""
TextType.TEXT: This should become a LeafNode with no tag, just a raw text value.
TextType.BOLD: This should become a LeafNode with a "b" tag and the text
TextType.ITALIC: "i" tag, text
TextType.CODE: "code" tag, text
TextType.LINK: "a" tag, anchor text, and "href" prop
TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
"""


def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("Invalid argument: requires a TextNode")
    leaf_node = None
    if text_node.text_type == TextType.TEXT:
        leaf_node = LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        leaf_node = LeafNode('b', text_node.text)
    if text_node.text_type == TextType.ITALIC:
        leaf_node = LeafNode('i', text_node.text)
    if text_node.text_type == TextType.CODE:
        leaf_node = LeafNode('code', text_node.text)

    return leaf_node

