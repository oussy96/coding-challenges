from argparse import Namespace
import io
import unittest
from cccat import cc_cat, read_input, read_input_nb_lines, read_input_nb_exc_nb_lines
import sys


class TestCccat(unittest.TestCase):

    def test_file1(self):
        self.assertEqual(cc_cat(Namespace(filename=['test.txt'], read=False, number=False, bnumber=False))
                         , '''"Your heart is the size of an ocean. Go find yourself in its hidden depths."
"The Bay of Bengal is hit frequently by cyclones. The months of November and May, in particular, are dangerous in this regard."
"Thinking is the capital, Enterprise is the way, Hard Work is the solution."
"If You Can'T Make It Good, At Least Make It Look Good."
"Heart be brave. If you cannot be brave, just go. Love's glory is not a small thing."
"It is bad for a young man to sin; but it is worse for an old man to sin."
"If You Are Out To Describe The Truth, Leave Elegance To The Tailor."
"O man you are busy working for the world, and the world is busy trying to turn you out."
"While children are struggling to be unique, the world around them is trying all means to make them look like everybody else."
"These Capitalists Generally Act Harmoniously And In Concert, To Fleece The People."
''')

    def test_file2(self):
        self.assertEqual(cc_cat(Namespace(filename=['test2.txt'], read=False, number=False, bnumber=False))
                         , '''"I Don'T Believe In Failure. It Is Not Failure If You Enjoyed The Process."
"Do not get elated at any victory, for all such victory is subject to the will of God."
"Wear gratitude like a cloak and it will feed every corner of your life."
"If you even dream of beating me you'd better wake up and apologize."
"I Will Praise Any Man That Will Praise Me."
"One Of The Greatest Diseases Is To Be Nobody To Anybody."
"I'm so fast that last night I turned off the light switch in my hotel room and was in bed before the room was dark."
"People Must Learn To Hate And If They Can Learn To Hate, They Can Be Taught To Love."
"Everyone has been made for some particular work, and the desire for that work has been put in every heart."
"The less of the World, the freer you live."
''')
        
    def test_files(self):
        self.assertEqual(cc_cat(Namespace(filename=['test.txt', 'test2.txt'], read=False, number=False, bnumber=False))
                         , '''"Your heart is the size of an ocean. Go find yourself in its hidden depths."
"The Bay of Bengal is hit frequently by cyclones. The months of November and May, in particular, are dangerous in this regard."
"Thinking is the capital, Enterprise is the way, Hard Work is the solution."
"If You Can'T Make It Good, At Least Make It Look Good."
"Heart be brave. If you cannot be brave, just go. Love's glory is not a small thing."
"It is bad for a young man to sin; but it is worse for an old man to sin."
"If You Are Out To Describe The Truth, Leave Elegance To The Tailor."
"O man you are busy working for the world, and the world is busy trying to turn you out."
"While children are struggling to be unique, the world around them is trying all means to make them look like everybody else."
"These Capitalists Generally Act Harmoniously And In Concert, To Fleece The People."
"I Don'T Believe In Failure. It Is Not Failure If You Enjoyed The Process."
"Do not get elated at any victory, for all such victory is subject to the will of God."
"Wear gratitude like a cloak and it will feed every corner of your life."
"If you even dream of beating me you'd better wake up and apologize."
"I Will Praise Any Man That Will Praise Me."
"One Of The Greatest Diseases Is To Be Nobody To Anybody."
"I'm so fast that last night I turned off the light switch in my hotel room and was in bed before the room was dark."
"People Must Learn To Hate And If They Can Learn To Hate, They Can Be Taught To Love."
"Everyone has been made for some particular work, and the desire for that work has been put in every heart."
"The less of the World, the freer you live."
''')
        
    def test_input(self):
        sys.stdin = io.StringIO("test")
        self.assertEqual(read_input(sys.stdin)
                         , 'test'.strip())
    
    def test_input_number(self):
        sys.stdin = io.StringIO("test\n\ntest")
        self.assertEqual(read_input_nb_lines(sys.stdin)
                         , '''1 test\n2\n3 test''')
    
    def test_input_bnumber(self):
        sys.stdin = io.StringIO("test\n\ntest")
        self.assertEqual(read_input_nb_exc_nb_lines((sys.stdin))
                         , "1 test\n\n2 test")
        
if __name__ == '__main__':
    unittest.main()
