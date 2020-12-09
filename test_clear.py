from bs4 import BeautifulSoup as bs
import unittest


class testClear(unittest.TestCase):
    
    # This test will check a simple clear call and we want to see if it clears as specified in the documentation
    def test_simple_clear(self):
        soup = bs("<a href=test>TEST TEST<i>test</i></a>", 'html.parser')
        tag = soup.a
        tag.clear()
        self.assertEqual(str(tag), '<a href="test"></a>')

    # This test checks if we give clear an empty tag if he returns an empty tag
    def test_clear_empty(self):
        soup = bs("<a></a>", 'html.parser')
        tag = soup.a
        tag.clear()
        self.assertEqual(str(tag), '<a></a>')

if __name__ == '__main__':
    unittest.main()