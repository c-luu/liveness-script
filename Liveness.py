import csv

class Liveness():
    def __init__(self
                , succs
                , defs
                , uses
                , live_in
                , live_out):
        self._succs = succs
        self._defs = defs
        self._uses = uses
        self._live_in = live_in
        self._live_out = live_out
        self._instructions = []

    def out_set(self, inst):
        return { inst : reduce(set.union, 
                               map(lambda k: self._live_in[k]
                               , self._succs[inst])) }

    def in_set(self, inst):
        return { inst : self._live_out[inst]
                            .difference(self._defs[inst])
                            .union(self._uses[inst]) }

    def load(self, file_name):
        with open(file_name, 'rb') as ir:
            for record in csv.DictReader(ir):
                self._instructions.append(int(record['inst']))
                self._succs[record['inst'].strip()] = set(map(lambda s: s.strip(), record['succ'].split(',')))
                self._defs[record['inst'].strip()] = set(map(lambda s: s.strip(), record['def'].split(',')))
                self._uses[record['inst'].strip()] = set(map(lambda s: s.strip(), record['use'].split(',')))
        print(self._instructions)
        print(self._succs)
        print(self._defs)
        print(self._uses)