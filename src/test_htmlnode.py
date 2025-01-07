import unittest

from htmlnode import HTMLNode, LeafNode

props = {
    "href": "https://www.google.com", 
    "target": "_blank",
    }


class TestTextNode(unittest.TestCase):
    def test_1(self):
        child_node = HTMLNode(tag="div", value="p")
        node = HTMLNode("p", "just some text and blabla",child_node, props)
        print(node.props_to_html())
        
    def test_2(self):
        node = HTMLNode(value="no tag, what is this madness")
        print(node)
        
    def test_3(self):
        node = HTMLNode(tag="img", props={"src":"blablub.com/yepyep.png"})
        print(node.props_to_html())
        
    def test_leaf_a(self):
        node = LeafNode("a", "Clickity Linkity",{"href":"einhoernchen.org"})
        print(node.to_html())
    
    def test_leaf_p(self):
        node = LeafNode("p", "paragraph textity text")
        print(node.to_html())
    
    def test_leaf_txt(self):
        node = LeafNode(tag=None,value="just some raaaaaaw text")
        print(node.to_html())
    
        
if __name__ == "__main__":
    unittest.main()