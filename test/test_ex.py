import sys
import unittest
from StringIO import StringIO

from src.learn_python_the_hard_way import ex_all


def test_ex01():
    print '\n*** Run the "Ex. 1" ***\n'
    ex_all.ex01()


def test_ex02():
    print '\n*** Run the "Ex. 2" ***\n'
    ex_all.ex02()



def test_ex03():
    print '\n*** Run the "Ex. 3" ***\n'
    ex_all.ex03()


def test_ex10():
    print '\n*** Run the "Ex. 10" ***\n'
    ex_all.ex10()


def test_ex11():
    print '\n*** Run the "Ex. 11" ***\n'
    ex_all.ex11()


def test_ex13():
    print '\n*** Run the "Ex. 13" ***\n'
    ex_all.ex13()


def test_ex15():
    print '\n*** Run the "Ex. 15" ***\n'
    ex_all.ex15()

def test_ex21():
    print '\n*** Run the "Ex. 21" ***\n'
    assert(ex_all.ex21_add(-1, 1) == 0)
    assert(ex_all.ex21_divide(3, 2) == 1)
       

class TestEx26(unittest.TestCase):

    def setUp(self):
        print '\n*** Run the "Ex. 26" ***\n'
        self.held = sys.stdout
        sys.stdout = StringIO()
        

    def tearDown(self):
        sys.stdout = self.held
        print '\n*** Done with "Ex.26" ***\n'
        

    def test_ex26(self):                  
        sentence = "All god\tthings come to those who weight."
        words = ex_all.Ex26.break_words(sentence)
        sorted_words = ex_all.Ex26.sort_words(words)
        ex_all.Ex26.print_first_word(words)        
        ex_all.Ex26.print_last_word(words)
        ex_all.Ex26.print_first_word(sorted_words)
        ex_all.Ex26.print_last_word(sorted_words)
        '''      
        sorted_words = ex_all.Ex26.sort_sentence(sentence)
        print sorted_words
        
        ex_all.Ex26.print_first_and_last(sentence)
        ex_all.Ex26.print_first_and_last_sorted(sentence)
        '''     
        lines = sys.stdout.getvalue().splitlines()
        self.assertEquals(lines[0], "All")
        self.assertEquals(lines[1], "weight.")
        self.assertEquals(lines[2], "All")
        self.assertEquals(lines[3], "who")


if __name__ == '__main__':
    import sys
    import nose
    print "Arguments are: ", str(sys.args[0])
    nose.main()