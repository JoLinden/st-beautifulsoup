from bs4 import BeautifulSoup
import re
import unittest


class BaseTestFindAll(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup('''<head><title>First element</title></head>
            <div class="second">Second element</div>
            <header class="blue" id="main_header">Other element</header>
            <div>Last element</div>''', 'html.parser')


class TestFindAllWithName(BaseTestFindAll):
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
             '<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    def test_match_tags_with_list(self):
        result = self.soup.find_all(['head', 'header'])

        self.assertListEqual(
            ['<head><title>First element</title></head>',
             '<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    def test_match_tags_with_function(self):
        def match_name(tag):
            return tag.has_attr('class')

        result = self.soup.find_all(match_name)

        self.assertListEqual(
            ['<div class="second">Second element</div>',
             '<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    def test_match_all_tags(self):
        result = self.soup.find_all(True)

        self.assertListEqual(
            ['<head><title>First element</title></head>',
             '<title>First element</title>',
             '<div class="second">Second element</div>',
             '<header class="blue" id="main_header">Other element</header>',
             '<div>Last element</div>'],
            list(map(str, result)))


class TestFindAllWithKeywordArgs(BaseTestFindAll):
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

    def test_tags_without_a_keyword_attribute(self):
        result = self.soup.find_all(class_=False)

        self.assertListEqual(
            ['<head><title>First element</title></head>',
             '<title>First element</title>',
             '<div>Last element</div>'],
            list(map(str, result)))

    def test_tags_with_multiple_keyword_attributes(self):
        result = self.soup.find_all(class_="blue", id="main_header")

        self.assertListEqual(
            ['<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    def test_attrs_keyword_argument(self):
        result = self.soup.find_all(attrs={'class': "blue"})

        self.assertListEqual(
            ['<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    def test_exact_class_names(self):
        soup = BeautifulSoup('''<div class="one two"></div>
        <span class="two one"></span>
        ''', 'html.parser')
        result = soup.find_all(attrs={'class': "one two"})

        self.assertListEqual(
            ['<div class="one two"></div>'],
            list(map(str, result)))


class TestFindAllWithStringArgument(BaseTestFindAll):
    def test_match_single_string(self):
        result = self.soup.find_all(string="Second element")

        self.assertListEqual(
            ['Second element'],
            list(map(str, result)))

    def test_match_multiple_strings(self):
        result = self.soup.find_all(string=['First element', 'Second element'])

        self.assertListEqual(
            ['First element', 'Second element'],
            list(map(str, result)))

    def test_match_strings_by_regex(self):
        result = self.soup.find_all(string=re.compile(r'st'))

        self.assertListEqual(
            ['First element', 'Last element'],
            list(map(str, result)))

    def test_match_strings_by_function(self):
        def match_function(s):
            return len(s) > 2 and s[1] in ['a', 'e']

        result = self.soup.find_all(string=match_function)

        self.assertListEqual(
            ['Second element', 'Last element'],
            list(map(str, result)))

    def test_find_all_strings(self):
        result = self.soup.find_all(string=True)

        self.assertListEqual(
            ['First element', '\n', 'Second element', '\n',
             'Other element', '\n', 'Last element'],
            list(map(str, result)))

    def test_match_tags_containing_string(self):
        self.soup.append(self.soup.new_tag('div'))
        result = self.soup.find_all(True, string=True)

        self.assertListEqual(
            ['<head><title>First element</title></head>',
             '<title>First element</title>',
             '<div class="second">Second element</div>',
             '<header class="blue" id="main_header">Other element</header>',
             '<div>Last element</div>'],
            list(map(str, result)))


class TestFindAllWithLimit(BaseTestFindAll):
    def test_limit_number_of_matches(self):
        result = self.soup.find_all(limit=2)

        self.assertEqual(len(result), 2)

    def test_limit_number_of_matches_for_specific_tag_name(self):
        result = self.soup.find_all('div', limit=1)

        self.assertListEqual(
            ['<div class="second">Second element</div>'],
            list(map(str, result)))

    def test_high_limit_number_of_matches_for_specific_tag_name(self):
        result = self.soup.find_all('div', limit=10)

        self.assertListEqual(
            ['<div class="second">Second element</div>',
             '<div>Last element</div>'],
            list(map(str, result)))


class TestFindAllWithRecursive(BaseTestFindAll):
    def test_child_element_with_no_recursive(self):
        result = self.soup.find_all('title', recursive=False)

        self.assertListEqual([], list(map(str, result)))

    def test_find_all_top_elements(self):
        result = self.soup.find_all(recursive=False)

        self.assertListEqual([
            '<head><title>First element</title></head>',
            '<div class="second">Second element</div>',
            '<header class="blue" id="main_header">Other element</header>',
            '<div>Last element</div>'], list(map(str, result)))


if __name__ == '__main__':
    unittest.main()
