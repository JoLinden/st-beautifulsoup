from bs4 import BeautifulSoup
import unittest


# Test the replace_with() method
class TestReplaceWith(unittest.TestCase):

    # We should be able to replace a string with a new string
    def test_replace_string_with_string(self):
        soup = BeautifulSoup('<i>Replace this text</i>', 'html.parser')

        soup.i.string.replace_with('Replaced text')

        self.assertEqual(soup,
                         BeautifulSoup('<i>Replaced text</i>', 'html.parser'))

    # We should be able to replace a string with a new tag
    def test_replace_string_with_tag(self):
        soup = BeautifulSoup('<i>This text should be an empty div tag</i>',
                             'html.parser')

        soup.i.string.replace_with(soup.new_tag('div'))

        self.assertEqual(soup,
                         BeautifulSoup('<i><div></div></i>', 'html.parser'))

    # We should be able to replace a tag with a new string
    def test_replace_tag_with_string(self):
        soup = BeautifulSoup('<i>This text should be a div tag</i>',
                             'html.parser')

        replacement = 'Just a string'
        soup.i.replace_with(replacement)

        self.assertEqual(soup,
                         BeautifulSoup(replacement, 'html.parser'))

    # We should be able to replace a tag with a new tag
    def test_replace_tag_with_tag(self):
        soup = BeautifulSoup('<div>Make <b>this</b> italic.</div>',
                             'html.parser')

        replacement = soup.new_tag('i')
        replacement.string = 'this'
        soup.b.replace_with(replacement)

        self.assertEqual(soup,
                         BeautifulSoup('<div>Make <i>this</i> italic.</div>',
                                       'html.parser'))


if __name__ == '__main__':
    unittest.main()
