frmin_impurity_decreaseom bs4 import BeautifulSoup
import unittest
"""Tag.unwrap() is the opposite of wrap().
It replaces a tag with whatever’s inside that tag.
It’s good for stripping out markup"""

class TestUnwrap(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup('''<head><title>First element</title></head>
                    <div class='second'>Second element</div>
                    <header>Other element</header>
                    <div>Last element</div>''', 'html.parser')

    def tearDown(self):
        pass

    # Test unwrapping a parent node
    def test_unwarp_outer(self):
        replaced = self.soup.head.unwrap()
        self.assertEqual(str(replaced), "<head></head>")
        with self.assertRaises(AttributeError):
            self.soup.head.unwrap() #Can't unwrap twice

    # Test unwrapping a child node
    def test_unwrap_inner(self):
        head_tag = self.soup.head
        unwrapped = head_tag.title.unwrap()
        self.assertEqual(str(unwrapped), "<title></title>")
        self.assertEqual(str(head_tag),"<head>First element</head>")

    # Test unwrapping something that does not exist in the soup
    def test_unwrap_nonexistant(self):
        with self.assertRaises(AttributeError):
            self.soup.p.unwrap()
        with self.assertRaises(AttributeError):
            self.soup.a.unwrap()

    # Test unwrapping a childless node
    def test_unwrap_single(self):
        unwrapped = self.soup.header.unwrap()
        self.assertEqual(str(unwrapped),"<header></header>")

    # Test unwrapping nodes with duplicate tags
    def test_unwrap_duplicate_tags(self):
        unwrapped = self.soup.div.unwrap()
        self.assertEqual(str(unwrapped),'<div class="second"></div>')
        unwrapped = self.soup.div.unwrap()
        self.assertEqual(str(unwrapped),'<div></div>')

    # Test unwrapping all tags in a simple HTML to get all the text
    def test_unwrap_all(self):
        self.soup.head.unwrap()
        self.soup.title.unwrap()
        self.soup.div.unwrap()
        self.soup.header.unwrap()
        self.soup.div.unwrap()
        self.assertEqual(str(self.soup), "First element\nSecond element\nOther element\nLast element")
if __name__ == '__main__':
    unittest.main()
