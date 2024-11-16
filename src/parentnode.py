from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        self.tag = tag
        self.children = children
        self.props = props
    
    def to_html(self):
        self.validate_members()
        child_nodes = self.generate_child_nodes()
        html = f"<{self.tag}"
        if self.props is None:
            html += ">"
        else:
            html += f"{self.generate_props()}>"
        for child in child_nodes:
            if isinstance(child, HTMLNode):
                html += child.to_html()
            else:
                html += child
        html += f"</{self.tag}>"
        return html

    def generate_child_nodes(self):
        if not isinstance(self.children,list) or (len(self.children) < 1):
            return []
        child_nodes = []
        for child in self.children:
            if isinstance(child, ParentNode):
                child_nodes.append(child.to_html())
            elif isinstance(child, LeafNode):
                child_nodes.append(child.to_html())
            elif isinstance(child, str):
                child_nodes.append(child)
        return child_nodes

    def validate_members(self):
        if self.children is None:
            raise ValueError("ParentNode children member must not be None")
        if self.tag is None:
            raise ValueError("ParentNode tag member must not be None")
        
    def generate_props(self):
        props_as_attributes = ""
        if self.props is not None:
            for prop in self.props:
                props_as_attributes += f" {prop}=\"{self.props[prop]}\"" 
        return props_as_attributes


