import csv

class Liveness():
    def __init__(self, succs, defs, uses, live_in, live_out):
        self._succs = succs
        self._defs = defs
        self._uses = uses
        self._live_in = live_in
        self._live_out = live_out

    def out_set(self, inst):
        return { inst : reduce(set.union, 
                               map(lambda k: self._live_in[k]
                               , self._succs[inst])) }

    def in_set(self, inst):
        return { inst : self._live_out[inst]
                            .difference(self._defs[inst])
                            .union(self._uses[inst]) }

