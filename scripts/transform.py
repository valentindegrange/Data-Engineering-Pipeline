from typing import Dict


def tranform(data: Dict) -> Dict:
  data['is_trasformed'] = True
  data['id'] = 1
  data['count'] = data['id'] + 1
  return data
