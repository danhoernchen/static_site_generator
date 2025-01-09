class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ''
        for key, value in self.props.items():
            result = result + f'{key}="{value}" '
        return result
    
    def __repr__(self):
        return f"{self.tag}\n{self.value}\n{self.children}\n{self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, props=props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        elif self.tag == None:
            return self.value
        elif self.props != None:
            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("Node must have a tag")
        if self.children == None:
            raise ValueError("Node must have children")
        elif self.props != None:
            children_string = self.__create_children_string(self.children)
            return f'<{self.tag} {self.props_to_html()}> {children_string} </{self.tag}>'
        else:
            children_string = self.__create_children_string(self.children)
            print(children_string)
            return f'<{self.tag}> {children_string} </{self.tag}>'
        
    def __create_children_string(self,children):
        children_string = ""
        for child in children:
                children_string = children_string + child.to_html()
        return children_string