from bs4 import BeautifulSoup
import unittest


class TestFindAll(unittest.TestCase):
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
        soup = BeautifulSoup('''<div>First element</div>
                             <div>Second element</div>
                             <span>Other element</span>''', 'html.parser')
        result = soup.find_all('div')

        self.assertListEqual(
            ['<div>First element</div>', '<div>Second element</div>'],
            list(map(str, result)))

    def test_matching_child(self):
        soup = BeautifulSoup('<div><span>First element</span></div>',
                             'html.parser')
        result = soup.find_all('span')

        self.assertListEqual(
            ['<span>First element</span>'],
            list(map(str, result)))

    def test_no_matches(self):
        soup = BeautifulSoup('<div>Not matching</div>', 'html.parser')
        result = soup.find_all('span')

        self.assertEqual(len(result), 0)

    def test_match_tag_with_attribute(self):
        soup = BeautifulSoup('''<div>First element</div>
                                     <div class="second">Second element</div>
                                     <span>Other element</span>''',
                             'html.parser')
        result = soup.find_all('div', 'second')

        self.assertListEqual(
            ['<div class="second">Second element</div>'],
            list(map(str, result)))


if __name__ == '__main__':
    unittest.main()
