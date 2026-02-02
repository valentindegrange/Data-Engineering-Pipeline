from typing import List
# this is my script extract file

def foo():
  print('foo')


def bar():
  print('bar')


def extract(data: List) -> List:
  new_data = list()
  keys = ['id', 'count', 'amount']
  
  for item in data:
    cropped_item = dict()
    for key, value in item.keys():
      if key in keys:
        cropped_item[key] = value
    new_data.append(cropped_item)

  return new_data 
        
