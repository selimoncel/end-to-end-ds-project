import os 

# python config box

#d = {"key1": "value1", "key2": "value2"}
#print(d['key2'])
#from box import ConfigBox
#d2 = ConfigBox({"key1": "value1", "key2": "value2"})
#print(repr(d2))


from ensure import ensure_annotations

@ensure_annotations
def get_product(x:int, y:int) -> int:
    return x*y

get_product(x = 2, y="3")