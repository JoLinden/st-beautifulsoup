from bs4 import BeautifulSoup
import unittest


class TestWrap(unittest.TestCase):
    def test_wrap_string(self):
        soup = BeautifulSoup('<p>I wish I was bold</p>', 'html.parser')

        soup.p.string.wrap(soup.new_tag('b'))
        self.assertEqual(soup,
                         BeautifulSoup('<p><b>I wish I was bold</b></p>',
                                       'html.parser'))

    def test_wrap_tag(self):
        soup = BeautifulSoup('<p>Test text</p>', 'html.parser')

        soup.p.wrap(soup.new_tag('div'))
        self.assertEqual(soup,
                         BeautifulSoup('<div><p>Test text</p></div>',
                                       'html.parser'))

    def test_wrap_tag_with_string(self):
        soup = BeautifulSoup('<p>Test text</p>', 'html.parser')
        self.assertRaises(Exception, soup.p.wrap, 'text')


if __name__ == '__main__':
    unittest.main()
