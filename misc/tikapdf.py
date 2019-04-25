#!/usr/bin/env python
import "/home/feline/.local/lib/python2.7/site-packages/tika"
from tika import parser
parsed = parser.from_file('/path/to/file')
print(parsed["metadata"])
print(parsed["content"])