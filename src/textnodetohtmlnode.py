from textnode import TextType, TextNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("Invalid argument: requires a TextNode")
    leaf_node = None
    if text_node.text_type == TextType.TEXT:
        leaf_node = LeafNode(None, text_node.text)
    return leaf_node

