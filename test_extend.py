from bs4 import BeautifulSoup as bs
import unittest


class testExtend(unittest.TestCase):
    
    def test_simple_extend(self):
        soup = bs("<a>TEST TEST</a>", 'html.parser')
        soup.a.extend([" ", "extended"])
        self.assertEqual(str(soup),"<a>TEST TEST extended</a>")
    
    def test_extend_nothing_passed(self):
        soup = bs("<a>Test</a>", 'html.parser')
        soup.a.extend([])
        self.assertEqual(str(soup),"<a>Test</a>")

    def test_contents(self):
        soup = bs("<a>TEST TEST</a>", 'html.parser')
        soup.a.extend(["extend", " "])
        get_content = soup.a.contents
        self.assertEqual(str(get_content), "['TEST TEST', 'extend', ' ']")

if __name__ == '__main__':
    unittest.main()