from bs4 import BeautifulSoup as bs
import unittest


class testFindAllNext(unittest.TestCase):
    
    # This test simply checks if we pass a value true if it finds all content of a given tag
    def test_simple(self):
        soup = bs("<a class = 'baiat' href = 'baiat.com/Test/Florin'>Test Florin<b>Aici</b></a>", 'html.parser')
        self.assertEqual(str(soup.a.find_all_next(string = True)), "['Test Florin', 'Aici']")  

    # This test checks if we have input a string value for find all next and if it returns the correct value
    def test_check_input_string_name(self):
        soup = bs("<a class = 'baiat' href = 'baiat.com/Test/Florin'>Test Florin<b>Aici</b></a>", 'html.parser')
        self.assertEqual(str(soup.a.find_all_next(string = "Aici")), "['Aici']")  

    # This test checks the attrs input when we give him a class name and we want to see if it returns the matching class
    def test_check_attrs(self):
        soup = bs("""<html><p class="body test"><a class="test"></a></p>
                    <p class="shape test">test</p>
                    <p class="into test">test1</p>
                    <p class="notest">test3</p></html>""", 'html.parser')
        get = soup.html.find_all_next(class_ = "test")
        self.assertEqual(str(get), '[<p class="body test"><a class="test"></a></p>, <a class="test"></a>, <p class="shape test">test</p>, <p class="into test">test1</p>]')

    # This test checks if we have input more than one attribute and if it returns the correct output
    def test_check_kwargs(self):
        soup = bs("""<html><p class="body test"><a class="test"></a></p>
                    <p class="shape test">test</p>
                    <p class="into test" id="link1">test1</p>
                    <p class="notest">test3</p></html>""", 'html.parser')
        get = soup.html.find_all_next(class_ = "test", string = "test1", id ="link1")
        self.assertEqual(str(get), '[<p class="into test" id="link1">test1</p>]')

    # This test checks the limit atribut by having an input a limit and checking if the output is only the limit or if it goves over
    def test_check_limit(self):
        soup = bs("""<html><p class="body test"><a class="test"></a></p>
                    <p class="shape test">test</p>
                    <p class="into test">test1</p>
                    <p class="notest">test3</p></html>""", 'html.parser')
        get = soup.html.find_all_next(class_ = "test", limit = 2)
        self.assertEqual(str(get), '[<p class="body test"><a class="test"></a></p>, <a class="test"></a>]')



if __name__ == '__main__':
    unittest.main()
