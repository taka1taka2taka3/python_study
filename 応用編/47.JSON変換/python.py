#オブジェクトからJSON文字列

import json

json_data = {'Python':'python-izm.com',
             'SearchEngine':('google.co.jp', 'yahoo.co.jp')}

print(type(json_data))

encode_json_data = json.dumps(json_data)

print(encode_json_data)
print(type(encode_json_data))



import json

json_data = {'Python':'python-izm.com',
             'SearchEngin':('google.co.jp', 'yahoo.co.jp')}

encode_json_data = json.dumps(json_data, indent=4)

print(encode_json_data)



#JSON文字列からオブジェクト

import json

json_data = {'Python':'python-izm.com',
             'SearchEngin':('google.co.jp', 'yahoo.co.jp')}

encode_json_data = json.dumps(json_data)
print(type(encode_json_data))

decode_json_data = json.loads(encode_json_data)
print(decode_json_data)
print(type(decode_json_data))
