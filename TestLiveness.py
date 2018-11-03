import unittest
import Liveness as liveness

class TestLiveness(unittest.TestCase):
    def setUp(self):
        pass

    def test_out_set(self):
        # import pdb; pdb.set_trace()

        # arrange
        succs = dict([ (0, { 0, 1}) ])
        defs = []
        uses = []
        live_in = dict([ (0, { 0 })
                          , (1, { 1, 2 }) ])
        live_out = []

        l = liveness.Liveness(succs, defs, uses, live_in, live_out)

        # act
        result = l.out_set(0) 

        # assert
        self.assertEqual(result, { 0: { 0, 1, 2 }})

if __name__ == '__main__':
        unittest.main()