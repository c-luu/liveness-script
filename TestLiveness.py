import unittest
import Liveness as liveness

class TestLiveness(unittest.TestCase):
    def setUp(self):
        pass

    def test_analyze(self):
        blocks = dict([('main': range(1, 7))
                       , ('label0': range(8, 9))
                       , ('labela': range(10, 25))
                       , ('labelb': range(26, 29))
                       , ('label2': range(30, 32))
                       , ('label3': range(33, 34))
                       , ('labelc': range(35, 36))
                       , ('labeld': range(37, 39))
                       , ('label1': range(44, 49))
                       , ('labele': range(50, 52))
                       , ('label6': range(54, 56))
                       ])
        flow_edges = dict([
                            ('main': { 'label0' })
                            , ('label0': { 'labela', 'label1' })
                            , ('labela': { 'labelb', 'label2' })
                            , ('labelb': { 'label3' })
                            , ('label2': { 'label3' })
                            , ('label3': { 'labelc', 'label4' })
                            , ('labelc': { 'labeld', 'label5' })
                            , ('labeld': { 'label5' })
                            , ('label5': { 'label3' })
                            , ('label4': { 'label0' })
                            , ('label1': { 'labele', 'label6' })
                            , ('label6': { 'label7' })
                            , ('labele': { 'label7' })
                            ])

        l = liveness.Liveness(file_name='ir.csv'
                                , blocks
                                , flow_edges)
        l.write('results.csv')

if __name__ == '__main__':
        unittest.main()