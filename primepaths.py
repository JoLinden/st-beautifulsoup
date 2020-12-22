#!/usr/bin/env python

from bs4 import BeautifulSoup, NavigableString
import unittest


class TestExtract(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup('''<head><title>First element</title></head>
                    <div class='second'>Second element</div>
                    <header>Other element</header>
                    <div>Last element</div>''', 'html.parser')

    def tearDown(self):
        pass

    # Prime path [1,2]
    def test_ins1(self):
        with self.assertRaises(ValueError):  # There is no head left
            self.soup.head.insert(1, None)

    # Prime path [1,3,4]
    def test_ins2(self):
        with self.assertRaises(ValueError):  # There is no head left
            self.soup.head.insert(1, self.soup.head)

    # Prime path [1,3,5,7,8,9]
    def test_insert(self):
        soup2 = BeautifulSoup('<header>another element</header>',
                              'html.parser')
        self.soup.div.insert(0, soup2)

        self.assertEqual(
            str(self.soup.div),
            '<div class="second"><header>another element</header>'
            'Second element</div>')

    # Prime path [1,3,5,6,7,10]
    def test_ins4(self):
        self.soup.div.insert(0, "Not a BeautifulSoup object")

        self.assertEqual(
            str(self.soup.div),
            '<div class="second">Not a BeautifulSoup object'
            'Second element</div>')

    # Prime path [1,3,5,7,10]
    def test_ins5(self):
        self.soup.div.insert(0, NavigableString("Not a BeautifulSoup object"))

        self.assertEqual(
            str(self.soup.div),
            '<div class="second">Not a BeautifulSoup object'
            'Second element</div>')

    # Prime path [1,3,5,7,8]
    def test_ins6(self):
        soup2 = BeautifulSoup('''''', 'html.parser')
        self.assertTrue(isinstance(soup2, BeautifulSoup))
        self.assertEqual(len(soup2.contents), 0) 
        self.soup.div.insert(0, soup2) 
        self.assertEqual(len(self.soup.div.contents), 1) 

    # Prime path [1,3,5,7,8,9,8,9,8]
    def test_ins7(self):
        soup2 = BeautifulSoup('<header>another element</header>'
                              '<div>Content</div>',
                              'html.parser')
        self.soup.div.insert(0, soup2)
        self.assertListEqual(['<header>another element</header>',
                              '<div>Content</div>',
                              'Second element'],
                             list(map(str, self.soup.div.contents)))


if __name__ == '__main__':
    unittest.main()
