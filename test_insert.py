from bs4 import BeautifulSoup
import unittest
class TestInsert(unittest.TestCase):
        def setUp(self):
            self.simple_soup = BeautifulSoup("<a><b><c>Hi, I'm a test</b></c><d> for y o u @ ! $ @ %</d></a>", 'html.parser')
        
        def test_insert_simple(self):
            self.simple_soup.a.insert(1, "Hai There")
            self.assertEqual(str(self.simple_soup), "<a><b><c>Hi, I'm a test</c></b>Hai There</a><d> for y o u @ ! $ @ %</d>")
        
        #A more complex test case checking elements position with previous() , next()
        def test_insert_prev_next(self):
            self.simple_soup.a.insert(0, "Hai There")
            newText = self.simple_soup.find(text="Hai There")
            self.assertEqual(str(newText.next), "<b><c>Hi, I'm a test</c></b>")
            self.assertEqual(newText.previous.next, newText)
        
        #Test float position index > 1
        def test_insert_float(self):
            self.simple_soup.a.insert(1.4352, "Hai There")
            #print(self.simple_soup)
            newText = self.simple_soup.find(text = "Hai There")
            self.assertEqual(newText.previous, "Hi, I'm a test")
        
        #Test float position index  where 0<=index<1
        def test_insert_float_zero(self):
            self.assertRaises(Exception, lambda: self.simple_soup.insert, 0.1231, "Hai There")
        
        #Test edge case of negative position value
        def test_insert_negative(self):
            self.assertRaises(Exception, lambda: self.simple_soup.insert, -1, "Hai There")
        
        #Test edge case where index value is larger than the number of elements
        def test_insert_posGreaterThanElements(self):
            self.simple_soup.a.insert(3, "Hai There")
            newText = self.simple_soup.find(text = "Hai There")
            self.assertEqual(newText.previous, "Hi, I'm a test")
            
if __name__ == '__main__':
    unittest.main()
    