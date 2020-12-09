from bs4 import BeautifulSoup
import unittest

class TestExtract(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup('''<head><title>First element</title></head>
                    <div class='second'>Second element</div>
                    <header>Other element</header>
                    <div>Last element</div>''', 'html.parser')

    def tearDown(self):
        pass

    # Test extracting a parent and a childless node
    def test_extract_basic_return(self):
        head = self.soup.head.extract()
        self.assertEqual("<head><title>First element</title></head>", str(head))
        header = self.soup.header.extract()
        self.assertEqual("<header>Other element</header>", str(header))

    # Test that extracting also deletes the node from the tree
    def test_extract_basic_delete(self):
        head = self.soup.head.extract()
        with self.assertRaises(AttributeError): # There is no head left
            self.soup.head.extract()

    # Test extracting something that does not exist
    def test_extract_nonexistant(self):
        with self.assertRaises(AttributeError):
            self.soup.p.extract()

    # Test extracting something with duplicate tags
    def test_extract_multiple1(self):
       div = self.soup.div.extract()
       self.assertEqual('<div class="second">Second element</div>', str(div))
       div = self.soup.div.extract()
       self.assertEqual("<div>Last element</div>", str(div))

    # Test that the extracted node is its own, unconnected sub-tree
    def test_extract_tree_split1(self):
        title = self.soup.title.extract()
        self.assertEqual(None,title.parent) #title is ophaned by extraction


    def test_extract_tree_split2(self):
        title = self.soup.title.extract()
        self.assertEqual([],list(self.soup.head.children))


    def test_extract_tree_split3(self):
        head = self.soup.head.extract()
        child = list(head.children)
        self.assertEqual("<title>First element</title>", str(child[0])) # Extracted node keeps its children
        with self.assertRaises(AttributeError):
            title = self.soup.title.extract() #Descendants are also removed from original tree

if __name__ == '__main__':
    unittest.main()
