import csv

class Liveness():
    def __init__(self
                 , succs = dict()
                 , defs = dict()
                 , uses = dict()
                 , live_in = dict()
                 , live_out = dict()
                 , file_name = ''):
        self._INST_COL = 'inst'
        self._DEF_COL = 'def'
        self._USE_COL = 'use'
        self._SUCC_COL = 'succ'
        self._IN_COL = 'live_in'
        self._OUT_COL = 'live_out'
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
                self._live_out[str(i)] = self.out_set(i)
                self._live_in[str(i)] = self.in_set(i)
                fix_point &= (pre_in_set == self._live_in.get(str(i), set())
                              and pre_out_set == self._live_out.get(str(i), set()))
        print('Fix-point reached in ' + str(iterations) + ' iterations.')

    def analyze_and_print_step(self, file_name):
        fix_point = False
        iterations = 0
        while (not fix_point):
            iterations += 1
            fix_point = True
            for i in self._instructions:
                pre_in_set = self._live_in.get(str(i), set())
                pre_out_set = self._live_out.get(str(i), set())
                self._live_out[str(i)] = self.out_set(i)
                self._live_in[str(i)] = self.in_set(i)
                fix_point &= (pre_in_set == self._live_in.get(str(i), set())
                              and pre_out_set == self._live_out.get(str(i), set()))
            self.write_step(file_name, iterations)


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
                self._instructions.append(int(record[self._INST_COL]))
                self._succs[record[self._INST_COL].strip()] = set(map(lambda s: s.strip(), record[self._SUCC_COL].split(',')))
                self._defs[record[self._INST_COL].strip()] = set(map(lambda s: s.strip(), record[self._DEF_COL].split(',')))
                self._uses[record[self._INST_COL].strip()] = set(map(lambda s: s.strip(), record[self._USE_COL].split(',')))

    def write_step(self, file_name, step):
        with open(file_name, 'a') as file:
            writer = csv.DictWriter(file
                                    , fieldnames = [self._INST_COL
                                                   , self._DEF_COL
                                                   , self._USE_COL
                                                   , self._SUCC_COL
                                                   , self._OUT_COL
                                                   , self._IN_COL ])
            file.write('STEP: ' + str(step) + '\n')
            writer.writeheader()
            [writer.writerow({
                self._INST_COL: str(i),
                self._DEF_COL: self.printableSet(self._defs.get(str(i), set())),
                self._USE_COL: self.printableSet(self._uses.get(str(i), set())),
                self._SUCC_COL: self.printableSet(self._succs.get(str(i), set())),
                self._OUT_COL: self.printableSet(self._live_out.get(str(i), set())),
                self._IN_COL: self.printableSet(self._live_in.get(str(i), set())),
            }) for i in self._instructions]

    def write(self, file_name):
        self.analyze()
        with open(file_name, 'w') as file:
            writer = csv.DictWriter(file
                                    , fieldnames = [self._INST_COL
                                                   , self._DEF_COL
                                                   , self._USE_COL
                                                   , self._SUCC_COL
                                                   , self._OUT_COL
                                                   , self._IN_COL ])
            writer.writeheader()
            [writer.writerow({
                self._INST_COL: str(i),
                self._DEF_COL: self.printableSet(self._defs.get(str(i), set())),
                self._USE_COL: self.printableSet(self._uses.get(str(i), set())),
                self._SUCC_COL: self.printableSet(self._succs.get(str(i), set())),
                self._OUT_COL: self.printableSet(self._live_out.get(str(i), set())),
                self._IN_COL: self.printableSet(self._live_in.get(str(i), set())),
            }) for i in self._instructions]

    def printableSet(self, s):
        return ','.join(filter(None, list(s)))

    def show(self):
        print(self._instructions)
        print(self._succs)
        print(self._defs)
        print(self._uses)
        print(self._live_in)
        print(self._live_out)
        print(map(lambda i: (str(i), self._live_in.get(str(i), set())), self._instructions))
        print(map(lambda i: (str(i), self._live_out.get(str(i), set())), self._instructions))