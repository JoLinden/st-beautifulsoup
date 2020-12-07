from bs4 import BeautifulSoup as bs
import unittest


class testClear(unittest.TestCase):
    
    def test_simple_clear(self):
        soup = bs("<a href=test>TEST TEST<i>test</i></a>", 'html.parser')
        tag = soup.a
        tag.clear()
        self.assertEqual(str(tag), '<a href="test"></a>')

    def test_clear_empty(self):
        soup = bs("<a>TEST TEST<i>test</i></a>", 'html.parser')
        tag = soup.a
        tag.clear()
        self.assertEqual(str(tag), '<a></a>')

    def test_clear_no_tag(self):
        soup = bs("<a></a>", 'html.parser')
        tag = soup.a
        tag.clear()
        self.assertEqual(str(tag), '<a></a>')


if __name__ == '__main__':
    unittest.main()