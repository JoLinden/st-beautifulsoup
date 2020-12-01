from bs4 import BeautifulSoup
import unittest


# Test that the wrap() method works as is explained in the documentation
class TestWrap(unittest.TestCase):

    # Make sure we can wrap a string with a tag
    def test_wrap_string(self):
        soup = BeautifulSoup('<p>I wish I was bold</p>', 'html.parser')

        soup.p.string.wrap(soup.new_tag('b'))
        self.assertEqual(soup,
                         BeautifulSoup('<p><b>I wish I was bold</b></p>',
                                       'html.parser'))

    # Make sure we can wrap a tag with another tag
    def test_wrap_tag(self):
        soup = BeautifulSoup('<p>Test text</p>', 'html.parser')

        soup.p.wrap(soup.new_tag('div'))
        self.assertEqual(soup,
                         BeautifulSoup('<div><p>Test text</p></div>',
                                       'html.parser'))

    # We should not be able to wrap a tag with a string, or anything that is
    # not a tag
    def test_wrap_tag_with_string(self):
        soup = BeautifulSoup('<p>Test text</p>', 'html.parser')
        self.assertRaises(Exception, soup.p.wrap, 'text')

        soup = BeautifulSoup('<p>Test text</p>', 'html.parser')
        self.assertRaises(Exception, soup.p.wrap, True)

        soup = BeautifulSoup('<p>Test text</p>', 'html.parser')
        self.assertRaises(Exception, soup.p.wrap, 1)

        soup = BeautifulSoup('<p>Test text</p>', 'html.parser')
        self.assertRaises(Exception, soup.p.wrap, [])


if __name__ == '__main__':
    unittest.main()
