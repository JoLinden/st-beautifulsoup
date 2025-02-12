from bs4 import BeautifulSoup
import unittest

class TestInsertInsertBeforeInsertAfterAndDecompose(unittest.TestCase):
        def setUp(self):
            self.simple_soup = BeautifulSoup("<a><b><c>Hi, I'm a test</b></c><d> for y o u @ ! $ @ %</d></a>", 'html.parser')
            self.simple_soup1 = BeautifulSoup("<a>hey hey</a><b>and</b><c>goodbye</c>", 'html.parser')
        
        ################################        Test insert()         #####################################
        
        #A really simple test case to check if we get expected output after applying insert as the documentation describes
        def test_insert_simple_string(self):
            self.simple_soup.a.insert(1, "Hai There")
            self.assertEqual(str(self.simple_soup), "<a><b><c>Hi, I'm a test</c></b>Hai There<d> for y o u @ ! $ @ %</d></a>")
        
        #A simple test to check if insert works for tag and if it handles correctly a tag as input
        def test_insert_simple_tag(self):
            tag = self.simple_soup.c
            tag.insert(0, 'its a tag ')
            self.simple_soup.insert(3, tag)
            #print(self.simple_soup)
            self.assertEqual(str(self.simple_soup),"<a><b></b><d> for y o u @ ! $ @ %</d></a><c>its a tag Hi, I'm a test</c>" )
            
        #A more complex test case checking elements position correctly
        def test_insert_positions_elements_correctly(self):
            self.simple_soup.a.insert(0, "Hai There")
            newText = self.simple_soup.find(text="Hai There")
            self.assertEqual(str(newText.next), "<b><c>Hi, I'm a test</c></b>")
            self.assertEqual(newText.previous.next, newText)
    
        #Test float position index  where 0<=index<1
        def test_insert_float_zero(self):
            self.assertRaises(Exception, lambda: self.simple_soup.insert, 0.1231, "Hai There")
        
        #Test edge case of negative position index
        def test_insert_negative(self):
            self.assertRaises(Exception, lambda: self.simple_soup.insert, -1, "Hai There")
        
        #Test edge case where index value is larger than the number of elements,
        #it will insert the new element after the last element
        def test_insert_posGreaterThanNumElements(self):
            self.simple_soup.a.insert(3, "Hai There")
            newText = self.simple_soup.find(text = "Hai There")
            self.assertEqual(newText.previous, " for y o u @ ! $ @ %")
        
        #Test that when we insert on empty tag it completes it and successfully inserts the element
        def test_insert_on_empty_element_tag(self):
            soup = BeautifulSoup("<a/>", "html.parser")
            soup.a.insert(1, "hej hej")
            self.assertEqual(str(soup.a), "<a>hej hej</a>")
        
        #################################     Test insert_before()     ######################################
        
        #A really simple test case to check if we get expected output after applying insert_before() as the documentation describes
        def test_insert_before_simple(self):
            self.simple_soup1.a.insert_before("Did I Say Hi?")
            self.simple_soup1.c.insert_before("Did I say goodbye?")
            self.assertEqual(str(self.simple_soup1), "Did I Say Hi?<a>hey hey</a><b>and</b>Did I say goodbye?<c>goodbye</c>")
        
        #A slightly more complex case, insert_before() but now parameter is a soup object tag
        def test_insert_before_element(self):
            self.simple_soup1.c.insert_before(self.simple_soup1.a)
            self.assertEqual(str(self.simple_soup1), "<b>and</b><a>hey hey</a><c>goodbye</c>")
        
        #Test insert_before() multiple values
        def test_insert_before_more_than_one(self):
            self.simple_soup1.a.insert_before("Did I Say Hi?", "I thought i did", "-_-", "Well, who cares?")
            self.simple_soup1.c.insert_before("Did I say goodbye", " (o_o) ", "Goodbyes are important", "Farewell then! : ) ")
            self.assertEqual(str(self.simple_soup1), "Did I Say Hi?I thought i did-_-Well, who cares?<a>hey hey</a><b>and</b>Did I say goodbye (o_o) Goodbyes are importantFarewell then! : ) <c>goodbye</c>")
            
            
        #Test insert_before(c) element tag c 
        def test_insert_before_same_element(self):
            self.simple_soup1.c.insert_before(self.simple_soup1.new_tag("c"))
            self.assertEqual(str(self.simple_soup1), "<a>hey hey</a><b>and</b><c></c><c>goodbye</c>" )
        
        #Test edge case to insert_before an element that has no parents
        def test_insert_before_no_parent(self):
            self.simple_soup1.a.extract()
            self.simple_soup1.b.extract()
            self.assertRaises(Exception, lambda: self.simple_soup1.c.insert_before, "let me in please")
        
        #Test edge case of inserting an element before itself
        def test_insert_element_before_itself(self):
            self.assertRaises(ValueError, self.simple_soup1.a.insert_before, self.simple_soup1.a)
        
        #Test that exception is raised when we insrt before "" in other word something "empty"
        def test_insert_before_something_empty(self):
            soup = BeautifulSoup("")
            tag = soup.new_tag("a")
            string = soup.new_string("")
            self.assertRaises(ValueError, string.insert_before, tag)
            self.assertRaises(NotImplementedError, soup.insert_before, tag)
            self.assertRaises(ValueError, tag.insert_before, tag)
            
        #################################     Test insert_after()     #####################################
        
        #A really simple test case to check if we get expected output after applying insert_after() as the documentation describes
        def test_insert_after_simple(self):
            self.simple_soup1.a.insert_after("Did I Say Hi?")
            self.simple_soup1.c.insert_after("Did I say goodbye?")
            self.assertEqual(str(self.simple_soup1), "<a>hey hey</a>Did I Say Hi?<b>and</b><c>goodbye</c>Did I say goodbye?")
       
        #A slightly more complex case, insert_after() but now element wise
        def test_insert_after_element(self):
            self.simple_soup1.c.insert_after(self.simple_soup1.a)
            self.assertEqual(str(self.simple_soup1), "<b>and</b><c>goodbye</c><a>hey hey</a>")
        
         #Test insert_after() multiple values
        def test_insert_after_more_than_one(self):
            self.simple_soup1.a.insert_after("Did I Say Hi?", "I thought i did", "-_-", "Well, who cares?")
            self.simple_soup1.c.insert_after("Did I say goodbye", " (o_o) ", "Goodbyes are important, ", "Farewell then! : ) ")
            self.assertEqual(str(self.simple_soup1), "<a>hey hey</a>Did I Say Hi?I thought i did-_-Well, who cares?<b>and</b><c>goodbye</c>Did I say goodbye (o_o) Goodbyes are important, Farewell then! : ) ")
        
        #Test insert_after(a) element a
        def test_insert_after_same_element(self):
            self.simple_soup1.a.insert_after(self.simple_soup1.new_tag("a"))
            self.assertEqual(str(self.simple_soup1), "<a>hey hey</a><a></a><b>and</b><c>goodbye</c>")
        
        #Test edge case to insert_after() element that has no parents
        def test_insert_after_no_parent(self):
           self.simple_soup1.b.extract()
           self.simple_soup1.c.extract()
           self.assertRaises(Exception, lambda: self.simple_soup1.a.insert_before, "let me in please")
        
        #Test edge case of inserting an element after itself
        def test_insert_element_after_itself(self):
            self.assertRaises(ValueError, self.simple_soup1.a.insert_after, self.simple_soup1.a)
        
        #Test that we get an exception when inserting after ""(i.e. nothing) in other words something empty
        def test_insert_after_something_that_has_no_meaning(self):
            soup = BeautifulSoup("")
            tag = soup.new_tag("a")
            string = soup.new_string("")
            self.assertRaises(ValueError, string.insert_after, tag)
            self.assertRaises(NotImplementedError, soup.insert_after, tag)
            self.assertRaises(ValueError, tag.insert_after, tag)
            
        ###############################      Test decompose()     #######################################
        
        #A simple Test to check decompose works as intended
        def test_decompose_tag(self):
            tag = self.simple_soup1.c
            tag.decompose()
            self.assertEqual(True, tag.decomposed)
            
        #Test that when you decompose a tag that is empty it doesnt destroy it
        def test_decompose_empty_tag(self):
            soup = BeautifulSoup('<a></a>', 'html.parser')
            tag = soup.a
            self.assertEqual(False, tag.decomposed)
            self.assertEqual(str(tag), '<a></a>')
        
        #An edge case test with empty nested tags decompose on inner tag
        def test_decompose_inner_empty_nested_tags(self):
            soup = BeautifulSoup('<a><b></b><d></d></a>', 'html.parser')
            b_tag = soup.b
            b_tag.decompose()
            self.assertEqual(True, b_tag.decomposed)
            self.assertEqual(str(soup),'<a><d></d></a>' )    
        
        #Similar as before but now decompose the outer element
        def test_decompose_outer_empty_nested_tags(self):
            soup = BeautifulSoup('<a><b></b><d></d></a>', 'html.parser')
            a_tag = soup.a
            a_tag.decompose()
            self.assertEqual(True, a_tag.decomposed)
            self.assertEqual(str(soup),'' )     
        
        
if __name__ == '__main__':
    unittest.main()       