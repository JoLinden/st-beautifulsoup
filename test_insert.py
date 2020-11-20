from bs4 import BeautifulSoup
import unittest

class TestInsertInsertBeforeInsertAfter(unittest.TestCase):
        def setUp(self):
            self.simple_soup = BeautifulSoup("<a><b><c>Hi, I'm a test</b></c><d> for y o u @ ! $ @ %</d></a>", 'html.parser')
            self.simple_soup1 = BeautifulSoup("<a>hey hey</a><b>and</b><c>goodbye</c>", 'html.parser')
        
        ################################        Test insert         #####################################
        
        #A really simple test case to check if we get expected output after applying insert as the documentation describes
        def test_insert_simple(self):
            self.simple_soup.a.insert(1, "Hai There")
            self.assertEqual(str(self.simple_soup), "<a><b><c>Hi, I'm a test</c></b>Hai There<d> for y o u @ ! $ @ %</d></a>")
        
        #A more complex test case checking elements position correctly
        def test_insert_positions_elements_correctly(self):
            self.simple_soup.a.insert(0, "Hai There")
            newText = self.simple_soup.find(text="Hai There")
            self.assertEqual(str(newText.next), "<b><c>Hi, I'm a test</c></b>")
            self.assertEqual(newText.previous.next, newText)
        
        #Test float position index > 1
        #def test_insert_float(self):
            #self.simple_soup.a.insert(1.4352, "Hai There")
            #print(self.simple_soup)
            #newText = self.simple_soup.find(text = "Hai There")
            #self.assertEqual(newText.previous, "Hi, I'm a test")
            
        #Test float position index  where 0<=index<1
        def test_insert_float_zero(self):
            self.assertRaises(Exception, lambda: self.simple_soup.insert, 0.1231, "Hai There")
        
        #Test edge case of negative position index
        def test_insert_negative(self):
            self.assertRaises(Exception, lambda: self.simple_soup.insert, -1, "Hai There")
        
        #Test edge case where index value is larger than the number of elements
        def test_insert_posGreaterThanNumElements(self):
            self.simple_soup.a.insert(3, "Hai There")
            newText = self.simple_soup.find(text = "Hai There")
            self.assertEqual(newText.previous, " for y o u @ ! $ @ %")
        
        #################################     Test insert_before()     ######################################
        
        #A really simple test case to check if we get expected output after applying insert_before() as the documentation describes
        def test_insert_before_simple(self):
            self.simple_soup1.a.insert_before("Did I Say Hi?")
            self.simple_soup1.c.insert_before("Did I say goodbye?")
            self.assertEqual(str(self.simple_soup1), "Did I Say Hi?<a>hey hey</a><b>and</b>Did I say goodbye?<c>goodbye</c>")
        
        #A slightly more complex case, insert_before() but now element wise
        def test_insert_before_element(self):
            self.simple_soup1.c.insert_before(self.simple_soup1.a)
            self.assertEqual(str(self.simple_soup1), "<b>and</b><a>hey hey</a><c>goodbye</c>")
        
        #Test insert_before() multiple values
        def test_insert_before_more_than_one(self):
            self.simple_soup1.a.insert_before("Did I Say Hi?", "I thought i did", "-_-", "Well, who cares?")
            self.simple_soup1.c.insert_before("Did I say goodbye", " (o_o) ", "Goodbyes are important", "Farewell then! : ) ")
            self.assertEqual(str(self.simple_soup1), "Did I Say Hi?I thought i did-_-Well, who cares?<a>hey hey</a><b>and</b>Did I say goodbye (o_o) Goodbyes are importantFarewell then! : ) <c>goodbye</c>")
            
            
        #Test insert_before(a) element a 
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
            self.simple_soup1.c.insert_after("Did I say goodbye", " (o_o) ", "Goodbyes are important", "Farewell then! : ) ")
            self.assertEqual(str(self.simple_soup1), "<a>hey hey</a>Did I Say Hi?I thought i did-_-Well, who cares?<b>and</b><c>goodbye</c>Did I say goodbye (o_o) Goodbyes are importantFarewell then! : ) ")
        
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
        
        #####################################################################################################
            
if __name__ == '__main__':
    unittest.main()       
