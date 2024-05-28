import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_no_tag(self):
        test_leaf = LeafNode(None, "This is test text")
        self.assertEqual(test_leaf.to_html(), "This is test text")

    def test_no_value(self):
        test_leaf = LeafNode("p", None)
        with self.assertRaises(ValueError):
            test_leaf.to_html()

    def test_no_props_format(self):
        test_leaf = LeafNode("p", "Watching Dune part one")
        self.assertEqual(test_leaf.to_html(), "<p>Watching Dune part one</p>")

    def test_with_props_format(self):
        test_leaf = LeafNode("a", "Lets watch Dune part two", {"href": "https://www.dune2movielink.org"})
        self.assertEqual(test_leaf.to_html(), "<a href=\"https://www.dune2movielink.org\" >Lets watch Dune part two</a>")


if __name__ == "__main__":
    unittest.main()
