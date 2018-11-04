import csv

class Liveness():
    def __init__(self
                 , succs = dict()
                 , defs = dict()
                 , uses = dict()
                 , live_in = dict()
                 , live_out = dict()
                 , file_name = ''):
        self._instructions = []
        self._succs = succs
        self._defs = defs
        self._uses = uses
        self._live_in = live_in
        self._live_out = live_out

        if (file_name):
            self.load(file_name)

    def analyze(self):
        fix_point = False
        iterations = 0
        while (not fix_point):
            iterations += 1
            fix_point = True
            for i in self._instructions:
                pre_in_set = self._live_in.get(str(i), set())
                pre_out_set = self._live_out.get(str(i), set())
                self._live_in[str(i)] = self.in_set(i)
                self._live_out[str(i)] = self.out_set(i)

                fix_point &= (pre_in_set == self._live_in.get(str(i), set())
                             and pre_out_set == self._live_out.get(str(i), set()))

        print(iterations)


    def out_set(self, inst):
        return reduce(set.union, 
                        map(lambda k: self._live_in.get(str(k), set())
                        , self._succs.get(str(inst), set())))

    def in_set(self, inst):
        return self._live_out.get(str(inst), set()) \
                             .difference(self._defs.get(str(inst), set())) \
                             .union(self._uses.get(str(inst), set()))

    def load(self, file_name):
        with open(file_name, 'rb') as ir:
            for record in csv.DictReader(ir):
                self._instructions.append(int(record['inst']))
                self._succs[record['inst'].strip()] = set(map(lambda s: s.strip(), record['succ'].split(',')))
                self._defs[record['inst'].strip()] = set(map(lambda s: s.strip(), record['def'].split(',')))
                self._uses[record['inst'].strip()] = set(map(lambda s: s.strip(), record['use'].split(',')))

    def show(self):
        print(map(lambda i: (str(i), self._live_in.get(str(i), set())), self._instructions))
        '''
        print(self._instructions)
        print(self._succs)
        print(self._defs)
        print(self._uses)
        print(self._live_in)
        print(self._live_out)
        '''
