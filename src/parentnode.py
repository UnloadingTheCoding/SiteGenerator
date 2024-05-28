from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag")
        if self.children is None:
            raise ValueError("Missing children nodes")
        html_concat = ""
        for child in self.children:
            html_concat += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_concat}</{self.tag}>"

    def __repr__(self):
        return f"tag:{self.tag}, children:{self.children}, props:{self.props}"
