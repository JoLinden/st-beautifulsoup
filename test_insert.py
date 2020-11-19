from bs4 import BeautifulSoup
import unittest

class TestInsert(unittest.TestCase):
        #def setUp(self):
        # self.simple_soup = BeautifulSoup("<a><b><c>Hi, I'm a test</b></c><d> for y o u @ ! $ @ %</d></a>", 'html.parser')
        def test_insert(self):
            #A simple test to see if the soup is what we expect after insert
            soup = BeautifulSoup("<a><b><c>Hi, I'm a test</b></c><d> for y o u @ ! $ @ %</d></a>", 'html.parser')
            soup.a.insert(1, "Hai There")
            #print(soup)
            self.assertEqual(str(soup), "<a><b><c>Hi, I'm a test</c></b>Hai There</a><d> for y o u @ ! $ @ %</d>")
            
            #A more complex test case checking elements position with previous() , next()
            soup = BeautifulSoup("<a><b><c>Hi, I'm a test</b></c><d> for y o u @ ! $ @ %</d></a>", 'html.parser')
            soup.a.insert(0, "Hai There")
            newText = soup.find(text="Hai There")
            #print(newText.previous)
            self.assertEqual(str(newText.next), "<b><c>Hi, I'm a test</c></b>")
            self.assertEqual(newText.previous.next, newText)
           
            #Testing inserting a float as position, Works but it should not!
            soup = BeautifulSoup("<a><b><c>Hi, I'm a test</b></c><d> for y o u @ ! $ @ %</d></a>", 'html.parser')
            soup.d.insert(1.2012, "Hai There") #this should produce an error
            newText = soup.find(text="Hai There")
            self.assertEqual(newText.previous, " for y o u @ ! $ @ %") 
            
            #Testing inserting a float as position, Works but it should not!
            soup = BeautifulSoup("<a><b><c>Hi, I'm a test</b></c><d> for y o u @ ! $ @ %</d></a>", 'html.parser')
            soup.d.insert(2.2012, "Hai There") #this should produce an error
            newText = soup.find(text="Hai There")
            self.assertEqual(newText.previous, " for y o u @ ! $ @ %") 
            
            #Testing inserting a float as position but this time for 0.1
            #TypeError: list indices must be integers or slices, not float
            soup = BeautifulSoup("<a><b><c>Hi, I'm a test</b></c><d> for y o u @ ! $ @ %</d></a>", 'html.parser')
            soup.d.insert(0.1, "Hai There") #this produces an error as it should         
            newText = soup.find(text="Hai There")
            self.assertEqual(newText.previous.next, newText)
if __name__ == '__main__':
    unittest.main()
    
    