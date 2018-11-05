# liveness-script
Generates live-ness static analysis against intermediate representation.

## Lazy Usage
Change the input file in the test file if needed.

```
python TestLiveness
```

## Live-Ranges
A live-range is an intra-block def-use chain. If a variable is not redefined in block 1 and used in a successor block, the live-range is _closed_ in block 1. We open a new live-range at the _beginning_ of said successor block which closes at said use.

Idea: given _block 1_, if variable _a_ is used but not defined in _block 1_, consult either _live_ sets to determine range.

## Webs
_Webs_ are inter-block live-ranges for a variable's def-use chain. They have the following properties:

## Definitions
We need the following definitions to implement this:
* Domain of all defined variables.
* Block label -> instructions.
* Block label -> sucessor blocks.
* Instruction -> (definition, uses, sucessors).