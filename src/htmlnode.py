from enum import Enum

class HTMLNodeType(Enum):
    LINK = 'a'

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Yo, we've not implemented this yet")

    def props_to_html(self):
        attributes_string = " "
        if self.props != None:
            for prop in self.props:
                attributes_string += f"{prop}={self.props[prop]} "
        return attributes_string

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"
