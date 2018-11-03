# S := dict (I, { successors } )
# D := dict (I, { defs } )
# U := dict (I, { uses } )

# I := dict (I, { in } )
# O := dict (I, { out } )

# step 0: build succs dict
# step 1: build def and use dicts
# step 2: build out dict
# step 3: build in dict

# out_set : int -> (key: int, val: { string })
'''
    var out = set()
    foreach s in Succs[i]:
        out.union(In[s])
    return out
'''
# in_set : int -> (key: int, val: { string })

