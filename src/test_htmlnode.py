import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        
    def test_parent_node(self):
        child1 = LeafNode("a", "Clickity Linkity",{"href":"einhoernchen.org"})
        child2 = LeafNode("p", "paragraph textity text")
        parent_node = ParentNode("div",[child1, child2])
        print(parent_node.to_html())
        
    def test_parent_node(self):
        child1 = LeafNode("a", "Clickity Linkity",{"href":"einhoernchen.org"})
        child2 = LeafNode("p", "paragraph textity text")
        parent_node1 = ParentNode("div",[child1, child2])
        child_3 = LeafNode(tag="img",value = "123", props={"src":"blablub.com/yepyep.png"})
        parent_node2 = ParentNode("div",[child_3, parent_node1],props = {"class":"container"})
        print(parent_node2.to_html())
        
    def test_parent_node(self):
        child1 = LeafNode("a", "Clickity Linkity",{"href":"einhoernchen.org"})
        child2 = LeafNode("p", "paragraph textity text")
        parent_node1 = ParentNode("div",[child1, child2])
        child_3 = LeafNode(tag="img",value = "123", props={"src":"blablub.com/yepyep.png"})
        parent_node2 = ParentNode("div",[child_3, parent_node1],props = {"class":"container"})
        child_4 = LeafNode("p","abcdef",{"class":"abc"})
        parent_node3 = ParentNode("div", [parent_node1, parent_node2])
        print(parent_node3.to_html())
    
        
if __name__ == "__main__":
    unittest.main()