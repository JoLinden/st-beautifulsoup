from bs4 import BeautifulSoup as bs
import unittest


class testExtend(unittest.TestCase):
    
    # This test checks if the extend funtion works as intender and adds the given inputs to the tag that we already have
    def test_simple_extend(self):
        soup = bs("<a>TEST TEST</a>", 'html.parser')
        soup.a.extend([" ", "extended"])
        self.assertEqual(str(soup),"<a>TEST TEST extended</a>")
    
    # This test checks if we have no input if it adds or not anything to the tag that we are trying to extend
    def test_extend_nothing_passed(self):
        soup = bs("<a>Test</a>", 'html.parser')
        soup.a.extend([])
        self.assertEqual(str(soup),"<a>Test</a>")

    # This test checks if the content of a tag is what suppose to be based on the documentation
    def test_contents(self):
        soup = bs("<a>TEST TEST</a>", 'html.parser')
        soup.a.extend(["extend", " "])
        get_content = soup.a.contents
        self.assertEqual(str(get_content), "['TEST TEST', 'extend', ' ']")

if __name__ == '__main__':
    unittest.main()