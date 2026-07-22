import json
data_json = '{"title": "Python工程师", "salary": "20k-40k", "city": "北京"}'

data = json.loads(data_json)
print(type(data))
print(data['title'])

py_dict = {"name": "张三", "age": 24, "city": "北京"}
json_str = json.dumps(py_dict, ensure_ascii=False)
print(type(json_str))
print(json_str)

