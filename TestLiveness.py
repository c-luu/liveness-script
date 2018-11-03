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

    def test_in_set(self):
        # import pdb; pdb.set_trace()

        # arrange
        succs = dict()
        defs = dict([ (0, { 0 }) ])
        uses = dict([ (0, { 1 }) ])
        live_in = dict()
        live_out = dict([ (0, { 0 }) ])

        l = liveness.Liveness(succs, defs, uses, live_in, live_out)

        # act
        result = l.in_set(0) 

        # assert
        self.assertEqual(result, { 0: { 1 } })

if __name__ == '__main__':
        unittest.main()