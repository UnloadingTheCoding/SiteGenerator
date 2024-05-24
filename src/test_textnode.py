import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("TestNode1", "italics")
        node2 = TextNode("TestNode2", "italics")
        self.assertNotEqual(node, node2)

    def test_almost_eq(self):
        node = TextNode("TestNode1", "italics")
        node2 = TextNode("TestNode1 ", "italics")
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("TestNode1", "italics", "https://internet.com")
        node2 = TextNode("TestNode1", "italics", "https://internet.com")
        self.assertEqual(node, node2)
        
    def test_url_not_eq(self):
        node = TextNode("TestNode1", "italics", "https://internet.com")
        node2 = TextNode("TestNode1", "italics")
        self.assertNotEqual(node, node2)

    def test_type_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_type_dif_case(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "Bold")
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()

