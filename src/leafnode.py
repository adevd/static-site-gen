from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props =None):
        super()
        self.tag = tag
        self.value = value
        self.children = None
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode requires a valid value")
        html_leaf = ""
        if self.tag is not None:
            html_leaf += f"<{self.tag}"
            if self.props is not None:
                html_leaf += f"{self.generate_props()}"
            html_leaf += ">"
        html_leaf += f"{self.value}"
        if self.tag is not None:
            html_leaf += f"</{self.tag}>"
        return html_leaf
        
    def generate_props(self):
        props_as_attributes = ""
        if self.props is not None:
            for prop in self.props:
                props_as_attributes += f" {prop}=\"{self.props[prop]}\"" 
        return props_as_attributes


