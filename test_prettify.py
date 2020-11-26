from bs4 import BeautifulSoup
import re
import unittest


class TestPrettify(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup('''<head><title>First element</title></head>
                    <div class='second'>Second element</div>
                    <header>Other element</header>
                    <div>Last element</div>''', 'html.parser')
        self.pretty = self.soup.prettify()
        self.pretty_split = [t.strip() for t in self.pretty.split("\n")]

    def tearDown(self):
        pass


    def test_first_elem(self):
        arr = self.pretty.split("\n")
        self.assertEqual(arr[0], "<head>")

    def test_indent(self):
        arr = self.pretty.split("\n")
        self.assertEqual(arr[1], " <title>")
        self.assertEqual(arr[2], "  First element")

    def test_open_tag(self):
        open_tags = ["<head>", "<title>", '<div class="second">', "<header>", "<div>"]
        for open_tag in open_tags:
            exist = open_tag in self.pretty_split
            self.assertTrue(exist)

    def test_closing_tag(self):
        closing_tags = ["</title>", "</head>", "</div>", "</header>"]
        for closing_tag in closing_tags:
            exist = closing_tag in self.pretty_split
            self.assertTrue(exist)


    def test_text(self):
        text = ["First element", "Second element", "Other element"]
        for t in text:
            exist = t in self.pretty_split
            self.assertTrue(exist)


if __name__ == '__main__':
    unittest.main()
