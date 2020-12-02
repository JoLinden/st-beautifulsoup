from bs4 import BeautifulSoup as bs
import unittest

class TestFindNext(unittest.TestCase):
    
    def test_simple_given_find(self):
        soup = bs("<div><h1>Big Heading</h1><p>P tag with stuff</p><h2>Second heading</h2><p>Second p tag</p><footer>Footer stuff</footer></div>", "html.parser")
        self.assertEqual(soup.div.find_next("p").get_text(), "P tag with stuff")  
        
    def test_simple_find_no_param(self):
        soup = bs("""<div><h1 id="test">Big Heading</h1><p>P tag with stuff</p><h2>Second heading</h2><p>Second p tag</p><footer>Footer stuff</footer></div>""", "html.parser")
        self.assertEqual(soup.div.find_next().get_text(), "Big Heading") 
        self.assertEqual(soup.div.find_next()["id"], "test") 
        
    def test_find_fake_tag(self): 
        soup = bs("<div> <faketag> this is a fake tag </faketag> </div>", "html.parser")
        fake_tag = soup.div.find_next()
        self.assertIn("<faketag> this is a fake tag </faketag>", str(fake_tag))
        self.assertEqual(fake_tag.get_text(), " this is a fake tag ")

    def test_find_chain(self): 
        soup = bs("<div> <p>first ptag</p><p>second ptag</p><p>third ptag</p> </div>", "html.parser")
        self.assertEqual("<p>first ptag</p>", str(soup.div.contents[0].find_next()))
        self.assertEqual("<p>second ptag</p>", str(soup.div.contents[1].find_next()))
        self.assertEqual("<p>third ptag</p>", str(soup.div.contents[2].find_next()))

    def test_find_string(self): 
        soup = bs("<div><h1>First heading</h1><p>Hello world</p><p>second p tag</p></div>", "html.parser")
        first_string_found = soup.div.find_next(string=True)
        self.assertEqual("First heading", first_string_found)

    # These 3 tests use the class and id find attribute to show that it will find
    # the next upcoming tag that matches the sent in attribute
    def test_find_next_class(self): 
        soup = bs("""<div><p>first p tag, no attr</p><p class="p1">second p tag</p><p class="p2">third p tag</p></div>""", "html.parser") 
        # Will skip the first p tag which is actually the next from div tag
        find_on_class = soup.div.find_next(class_="p1")
        find_on_class2 = soup.div.find_next(class_="p2")
        self.assertIn("second p tag", find_on_class.get_text())
        self.assertIn("third p tag", find_on_class2.get_text())

    def test_find_next_id(self): 
        soup = bs("""<div><p>first p tag, no attr</p><p id="p1">second p tag</p><p id="p2">third p tag</p></div>""", "html.parser") 
        find_on_id = soup.div.find_next(id="p1")
        self.assertEqual("second p tag", find_on_id.get_text())
    
    def test_find_next_ignore_id(self): 
        soup = bs("""<div><p>first p tag, no attr</p><p id="p1">second p tag</p><p id="p2">third p tag</p></div>""", "html.parser") 
        find_next_p = soup.div.find_next("p")
        self.assertEqual("first p tag, no attr", find_next_p.get_text())



if __name__ == "__main__": 
    unittest.main() 
