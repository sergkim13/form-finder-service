from urllib.parse import parse_qsl

params_string='f_name1=value1&f_name2=value2'
res = parse_qsl(params_string)
print(dict(res))
