# this is my script extract file

def foo():
  print('foo')


def bar():
  print('bar')


def extract(data: dict):
  keys = ['id', 'count', 'amount']
  new_data = dict()
  for k in keys:
    new_data[k] = data[k]
  return new_data
