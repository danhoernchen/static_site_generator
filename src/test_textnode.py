import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("YabbaDabbaURL", TextType.LINK,"www.google.com")
        node2 = TextNode("YabbaDabbaURL", TextType.LINK,"www.google.com")
        self.assertEqual(node, node2)
        
    def test_eqImg(self):
        node = TextNode("YabbaDabbaImage", TextType.IMAGE)
        node2 = TextNode("YabbaDabbaImage", TextType.IMAGE)
        self.assertEqual(node, node2)
    
    def test_eqNone(self):
        node = TextNode("YabbaDabbaNone", TextType.LINK, None)
        node2 = TextNode("YabbaDabbaNone", TextType.LINK, None)
        self.assertEqual(node, node2)
        
    def test_eqDif(self):
        node = TextNode("YabbaDabba1", TextType.CODE)
        node2 = TextNode("YabbaDabba2", TextType.CODE)
        self.assertNotEqual(node, node2)
        
    def test_eqDifType(self):
        node = TextNode("YabbaDabbaNone", TextType.LINK, None)
        node2 = TextNode("YabbaDabbaNone", TextType.IMAGE, None)
        self.assertNotEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()