from bs4 import BeautifulSoup
import re
import unittest


class TestFindAllWithName(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup('''<head><title>First element</title></head>
                    <div class="second">Second element</div>
                    <header>Other element</header>
                    <div>Last element</div>''', 'html.parser')

    def test_exactly_one_element(self):
        soup = BeautifulSoup('<div>First element</div>', 'html.parser')
        result = soup.find_all('div')

        self.assertListEqual(['<div>First element</div>'],
                             list(map(str, result)))

    def test_exactly_two_elements(self):
        soup = BeautifulSoup('''<div>First element</div>
                             <div>Second element</div>''', 'html.parser')
        result = soup.find_all('div')

        self.assertListEqual(
            ['<div>First element</div>', '<div>Second element</div>'],
            list(map(str, result)))

    def test_two_matching_elements(self):
        result = self.soup.find_all('div')

        self.assertListEqual(
            ['<div class="second">Second element</div>',
             '<div>Last element</div>'],
            list(map(str, result)))

    def test_matching_child(self):
        result = self.soup.find_all('title')

        self.assertListEqual(
            ['<title>First element</title>'],
            list(map(str, result)))

    def test_no_matches(self):
        result = self.soup.find_all('span')

        self.assertEqual(len(result), 0)

    def test_match_tag_with_non_kwarg_class(self):
        result = self.soup.find_all('div', 'second')

        self.assertListEqual(
            ['<div class="second">Second element</div>'],
            list(map(str, result)))

    def test_match_tags_with_regex(self):
        result = self.soup.find_all(re.compile('head'))

        self.assertListEqual(
            ['<head><title>First element</title></head>',
             '<header>Other element</header>'],
            list(map(str, result)))

    def test_match_tags_with_list(self):
        result = self.soup.find_all(['head', 'header'])

        self.assertListEqual(
            ['<head><title>First element</title></head>',
             '<header>Other element</header>'],
            list(map(str, result)))

    def test_match_tags_with_function(self):
        def match_name(tag):
            return tag.has_attr('class')

        result = self.soup.find_all(match_name)

        self.assertListEqual(
            ['<div class="second">Second element</div>'],
            list(map(str, result)))

    def test_match_all_tags(self):
        result = self.soup.find_all(True)

        self.assertListEqual(
            ['<head><title>First element</title></head>',
             '<title>First element</title>',
             '<div class="second">Second element</div>',
             '<header>Other element</header>',
             '<div>Last element</div>'],
            list(map(str, result)))


class FindAllWithKeywordArgs(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup('''<head><title>First element</title></head>
            <div class="second">Second element</div>
            <header class="blue" id="main_header">Other element</header>
            <div>Last element</div>''', 'html.parser')

    def test_tags_containing_string(self):
        result = self.soup.find_all(string=re.compile(r'st\s'))

        self.assertListEqual(
            ['First element',
             'Last element'],
            list(map(str, result)))

    def test_keyword_attributes(self):
        result = self.soup.find_all(id="main_header")

        self.assertListEqual(
            ['<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    def test_tags_with_any_keyword_attributes(self):
        result = self.soup.find_all(class_=True)

        self.assertListEqual(
            ['<div class="second">Second element</div>',
             '<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))


if __name__ == '__main__':
    unittest.main()
