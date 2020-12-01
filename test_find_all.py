from bs4 import BeautifulSoup
import re
import unittest


# All find_all() tests will use the same test data, we pack this into one base
# test class
class BaseTestFindAll(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup('''<head><title>First element</title></head>
            <div class="second">Second element</div>
            <header class="blue" id="main_header">Other element</header>
            <div>Last element</div>''', 'html.parser')


# Test the first argument, name, of the find_all() method
class TestFindAllWithName(BaseTestFindAll):

    # Test the most basic case, one matching element should be returned, when
    # there only exists one matching element in the tree
    def test_exactly_one_element(self):
        soup = BeautifulSoup('<div>First element</div>', 'html.parser')
        result = soup.find_all('div')

        self.assertListEqual(['<div>First element</div>'],
                             list(map(str, result)))

    # Extend the above case to two matching elements
    def test_exactly_two_elements(self):
        soup = BeautifulSoup('''<div>First element</div>
                             <div>Second element</div>''', 'html.parser')
        result = soup.find_all('div')

        self.assertListEqual(
            ['<div>First element</div>', '<div>Second element</div>'],
            list(map(str, result)))

    # Test that only matching elements are returned
    def test_two_matching_elements(self):
        result = self.soup.find_all('div')

        self.assertListEqual(
            ['<div class="second">Second element</div>',
             '<div>Last element</div>'],
            list(map(str, result)))

    # Test that child elements can be found
    def test_matching_child(self):
        result = self.soup.find_all('title')

        self.assertListEqual(
            ['<title>First element</title>'],
            list(map(str, result)))

    # Make sure trying to find elements that does not exist returns an empty
    # list
    def test_no_matches(self):
        result = self.soup.find_all('span')

        self.assertEqual(len(result), 0)

    # The document mentions a second unnamed argument can be used to also match
    # an HTML class
    def test_match_tag_with_non_kwarg_class(self):
        result = self.soup.find_all('div', 'second')

        self.assertListEqual(
            ['<div class="second">Second element</div>'],
            list(map(str, result)))

    # Test matching by regex. Tags containing 'head' should be returned
    def test_match_tags_with_regex(self):
        result = self.soup.find_all(re.compile('head'))

        self.assertListEqual(
            ['<head><title>First element</title></head>',
             '<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    # Test matching by a list of tags. Tags matching either of the list
    # elements should be returned.
    def test_match_tags_with_list(self):
        result = self.soup.find_all(['head', 'header'])

        self.assertListEqual(
            ['<head><title>First element</title></head>',
             '<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    # Test matching by a function
    def test_match_tags_with_function(self):
        def match_name(tag):
            return tag.has_attr('class')

        result = self.soup.find_all(match_name)

        self.assertListEqual(
            ['<div class="second">Second element</div>',
             '<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    # Test match by True, should return all tags
    def test_match_all_tags(self):
        result = self.soup.find_all(True)

        self.assertListEqual(
            ['<head><title>First element</title></head>',
             '<title>First element</title>',
             '<div class="second">Second element</div>',
             '<header class="blue" id="main_header">Other element</header>',
             '<div>Last element</div>'],
            list(map(str, result)))


# Test the keyword arguments of the find_all() method, make sure we can find
# tags based on their HTML attributes
class TestFindAllWithKeywordArgs(BaseTestFindAll):

    # Test matching a keyword by a simple string
    def test_keyword_attributes(self):
        result = self.soup.find_all(id="main_header")

        self.assertListEqual(
            ['<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    # Test matching a keyword with True, should return all tags that has the
    # attribute with a value, regardless of its value
    def test_tags_with_any_keyword_attributes(self):
        result = self.soup.find_all(class_=True)

        self.assertListEqual(
            ['<div class="second">Second element</div>',
             '<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    # Test matching multiple keyword attributes, this should return only tags
    # matching both attributes
    def test_tags_with_multiple_keyword_attributes(self):
        result = self.soup.find_all(class_="blue", id="main_header")

        self.assertListEqual(
            ['<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    # It is possible to match keyword arguments with the attrs attribute, using
    # a dictionary instead. This should work the same way as using keyword
    # arguments
    def test_attrs_keyword_argument(self):
        result = self.soup.find_all(attrs={'class': "blue"})

        self.assertListEqual(
            ['<header class="blue" id="main_header">Other element</header>'],
            list(map(str, result)))

    # Matching by multiple class names is an exact match, meaning the order of
    # the class names matter
    def test_exact_class_names(self):
        soup = BeautifulSoup('''<div class="one two"></div>
        <span class="two one"></span>
        ''', 'html.parser')
        result = soup.find_all(attrs={'class': "one two"})

        self.assertListEqual(
            ['<div class="one two"></div>'],
            list(map(str, result)))


# Test the string argument of the find_all() method, to find matching strings,
# or tags containing matching strings
class TestFindAllWithStringArgument(BaseTestFindAll):

    # Find strings equal to a string
    def test_match_single_string(self):
        result = self.soup.find_all(string="Second element")

        self.assertListEqual(
            ['Second element'],
            list(map(str, result)))

    # Find strings equal to any of a list of strings
    def test_match_multiple_strings(self):
        result = self.soup.find_all(string=['First element', 'Second element'])

        self.assertListEqual(
            ['First element', 'Second element'],
            list(map(str, result)))

    # Find strings matching a regex
    def test_match_strings_by_regex(self):
        result = self.soup.find_all(string=re.compile(r'st'))

        self.assertListEqual(
            ['First element', 'Last element'],
            list(map(str, result)))

    # Find strings matching a function
    def test_match_strings_by_function(self):
        def match_function(s):
            return len(s) > 2 and s[1] in ['a', 'e']

        result = self.soup.find_all(string=match_function)

        self.assertListEqual(
            ['Second element', 'Last element'],
            list(map(str, result)))

    # Find all strings, using string=True
    def test_find_all_strings(self):
        result = self.soup.find_all(string=True)

        self.assertListEqual(
            ['First element', '\n', 'Second element', '\n',
             'Other element', '\n', 'Last element'],
            list(map(str, result)))

    # Find all tags containing a string. We first append an empty tag that
    # should not be returned by find_all()
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


# Test the limit argument of the find_all() method, to limit the number of
# matches returned by the method
class TestFindAllWithLimit(BaseTestFindAll):

    # Find all elements, but limit the result to 2. We expect exactly two
    # elements to be returned.
    def test_limit_number_of_matches(self):
        result = self.soup.find_all(limit=2)

        self.assertEqual(len(result), 2)

    # Find tags matching a name, but limit the result to 1. We expect the first
    # matching element to be returned.
    def test_limit_number_of_matches_for_specific_tag_name(self):
        result = self.soup.find_all('div', limit=1)

        self.assertListEqual(
            ['<div class="second">Second element</div>'],
            list(map(str, result)))

    # Set a limit higher than the number of elements that can be found. All
    # matching elements should be returned.
    def test_high_limit_number_of_matches_for_specific_tag_name(self):
        result = self.soup.find_all('div', limit=10)

        self.assertListEqual(
            ['<div class="second">Second element</div>',
             '<div>Last element</div>'],
            list(map(str, result)))


# Test the recursive argument of the find_all() method, to either only find
# direct descendants, or find all tags in a tree
class TestFindAllWithRecursive(BaseTestFindAll):

    # Set recursive=False to only find top level elements. Trying to find an
    # element we know is a child should return an empty list.
    def test_child_element_with_no_recursive(self):
        result = self.soup.find_all('title', recursive=False)

        self.assertListEqual([], list(map(str, result)))

    # Set recursive=False and find all elements. This should only return top
    # level elements with their contents. Child elements should not be returned
    # isolated from their parents.
    def test_find_all_top_elements(self):
        result = self.soup.find_all(recursive=False)

        self.assertListEqual([
            '<head><title>First element</title></head>',
            '<div class="second">Second element</div>',
            '<header class="blue" id="main_header">Other element</header>',
            '<div>Last element</div>'], list(map(str, result)))


if __name__ == '__main__':
    unittest.main()
