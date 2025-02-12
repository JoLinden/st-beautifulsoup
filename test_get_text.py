from bs4 import BeautifulSoup as bs
import unittest

class TestGetText(unittest.TestCase):
    # Simple usage of the get_text method, returns some html tags content
    def test_simple(self): 
        soup = bs("<p>Hello World!</p>", "html.parser") 
        self.assertEqual(soup.get_text(), "Hello World!")  

    # Using the get_text method on html that contains multiple elements
    def test_large_html(self): 
        soup = bs("<div><h1>Big heading </h1><p>Small p tag</p></div>", "html.parser") 
        allHtml = soup.get_text().split(" ") 
        self.assertEqual(len(allHtml), 5)

        new_footer = soup.new_tag("footer") 
        new_footer.string = " Heeeeey"
        soup.append(new_footer)
        allHtmlNew = soup.get_text().split(" ") 
        self.assertEqual(len(allHtmlNew), 6)
        self.assertIn("Big heading", soup.get_text())
        self.assertEqual(soup.div.p.get_text(), "Small p tag") 

    # Testing what happens if the given html content is empty
    def test_get_empty(self):
        soup = bs("", "html.parser") 
        allHtml = soup.get_text()
        self.assertEqual(allHtml, "")  
    
    # Testing how the method works when selecting a specific element inside a parent element
    def test_get_nested(self):
        soup = bs("<div><h1>heading 1</h1><p>stuff here</p></div>", "html.parser") 
        pHtml = soup.div.p.get_text()
        self.assertIn("stuff here", pHtml)
        self.assertEqual("stuff here", pHtml) 

    # Testing how it works if there are 2 similar elements, which will the method return
    def test_get_nested_duplicate(self): 
        soup = bs("<div><p>First p tag</p><p>Second p tag</p></div>", "html.parser")
        # Will get the first p tag it finds in the given html
        pHtml = soup.div.p.get_text()
        self.assertIn("First p tag", pHtml)     

    # Testing the method based on finding the element by id
    def test_get_id(self): 
        soup = bs("""<div><p>first p tag</p><p id="test">second p tag</p></div>""", "html.parser") 
        pHtmlWithID = soup.div.find(id="test").get_text()
        pHtmlNoID = soup.div.p.get_text() 
        self.assertIn("second p tag", pHtmlWithID)
        self.assertIn("first p tag", pHtmlNoID)
    
    # Testing method based on finding an id when there are several that are the same
    def test_get_duplicate_id(self):
        soup = bs("""<div><p id="p1">first p tag</p><p id="p1">second p tag</p></div>""", "html.parser") 
        p_tag = soup.div.find(id="p1").get_text()
        self.assertIn(p_tag, soup.div.contents[0])
        self.assertNotIn(p_tag, soup.div.contents[1])

    # Testing the method on some fake html tag
    def test_get_fake_html_tag(self): 
        soup = bs("<div><faketag> This is a fake tag </faketag> <p> Real p tag </p> </div>", "html.parser")
        fake_tag = soup.div.faketag.get_text()
        self.assertEqual(" This is a fake tag ", fake_tag)

    # Testing the method based on finding based on a class 
    def test_get_class(self): 
        soup = bs("""<div> <p class="p1">Hello<p> </div>""", "html.parser")
        get_tag_class = soup.div.find(class_="p1").get_text() 
        self.assertIn("Hello", get_tag_class)


if __name__ == "__main__": 
    unittest.main()



