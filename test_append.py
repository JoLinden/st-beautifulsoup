from bs4 import BeautifulSoup as bs
import unittest

class TestAppend(unittest.TestCase): 

    def test_string_append(self):
        soup = bs("<p>Hello World,</p>", "html.parser")    
        new_string = "Hi there"
        soup.p.append(new_string)
        self.assertEqual(len(soup.p.contents), 2)
        self.assertEqual(soup.p.contents[0], "Hello World,") 
        self.assertEqual(soup.p.contents[1], "Hi there")        
       
    def test_append_tag(self): 
        soup = bs("<div> Start of a tag </div>", "html.parser")
        new_p_tag = soup.new_tag("p")
        new_p_tag.string = "This tag was added in the parent"
        soup.div.append(new_p_tag)
        
        self.assertEqual(len(soup.contents), 1) 
        self.assertIn(new_p_tag, soup.div) 
        self.assertIn("This tag was added in the parent", new_p_tag.string)
        self.assertEqual(len(soup.div.contents), 2) 
      
    def test_append_with_id(self): 
        soup = bs("""<div id="test1"><h1> Title of something </h1></div>""", "html.parser")
        new_p_tag = soup.new_tag("p")
        new_p_tag.string = "Testing new p tag" 
        soup.find(id="test1").append(new_p_tag)
       
        self.assertIn(new_p_tag, soup.div) 
        self.assertEqual(len(soup.div.contents), 2)
        self.assertEqual(soup.div.h1.next_sibling, new_p_tag)
    
    def test_append_empty(self): 
        soup = bs("", "html.parser")
        soup.append("hello world")
        self.assertEqual(len(soup.contents), 1) 
        self.assertIn("hello world", soup)
       
    def test_append_to_fake_html_tag(self): 
        soup = bs("<div><faketag> This is not a real html tag </faketag></div>", "html.parser")
        new_fake_tag = soup.new_tag("newTag")
        new_fake_tag.string = "This is also a fake tag"
        soup.div.append(new_fake_tag)
        soup.div.faketag.append("appending to original fake tag")

        self.assertEqual(len(soup.div.faketag.contents), 2)
        self.assertEqual(len(soup.div.contents), 2)
        self.assertIn(new_fake_tag, soup.div)
    
    def test_append_order(self): 
        soup = bs("""<div><h1>First h1</h1><p id="p1">Hello world </p><p id="p2">Other p tag </p></div>""", "html.parser")
        new_tag = soup.new_tag("testTag")
        new_tag.string = "Which p tag is this appended to?"
        soup.div.p.append(new_tag)
        self.assertIn(new_tag, soup.find(id="p1"))
        self.assertNotIn(new_tag, soup.find(id="p2"))
    
    def test_lots_of_appends(self): 
        soup = bs("<div></div>", "html.parser")
        for _ in range(0, 200): 
            new_tag = soup.new_tag("loopTag")
            soup.div.append(new_tag)
        self.assertEqual(len(soup.div.contents), 200)
        

if __name__ == "__main__": 
    unittest.main()
