
class HTMLNode:

    def __init__(self, tag: str = None, value=None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        attribute = ""
        if self.props == None:
            return attribute
        for pro in self.props:
            attribute += f"{pro}=\"{self.props[pro]}\" "
        return attribute

    def __repr__(self):
        rep = f"tag={self.tag}, value={self.value} children="
        for child in self.children:
            rep += f"{child.tag} "
        rep += f"props={self.props_to_html}"

