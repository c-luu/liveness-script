import unittest
import Liveness as liveness

class TestLiveness(unittest.TestCase):
    def setUp(self):
        pass

    def test_analyze(self):
        l = liveness.Liveness(file_name='ir.csv')
        l.analyze_and_print_step('steps.csv')

if __name__ == '__main__':
        unittest.main()