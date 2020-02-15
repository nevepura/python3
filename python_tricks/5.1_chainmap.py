from collections import ChainMap

# Notice: I can have same key:value couple in the dictionaries, and I am still allowed to chain them
dict1 = {"one":1, "two":2, "three":3}
dict2 = {"two":2, "three":3, "four":4.0}

chain = ChainMap(dict1, dict2)

"""
print(chain["one"])
print(chain["two"])
print(chain["three"])
print(chain["four"])
"""

# Lookup (= read) searchs all dictionaries of the ChainMap. 
# insert, update, delete only affect the first dictionary of the ChainMap (why?)
print(f"initial chain: {chain}")

del(chain["two"])
print(chain["two"])
# del(chain['two']) # KeyError: "Key not found in the first mapping: 'two'"
chain['two'] = "new two" # insert affects dict1
chain['two'] = "two updated" # update affects dict1

print(f"final chain: {chain}")