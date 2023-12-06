import json

with open('conf.json') as conf_file:
  file_contents = conf_file.read()
  
print(file_contents)

parsed_json = json.loads(file_contents)
for stock in parsed_json:
  if 'name' in stock:
    print(f"Symbol:{stock['name']},\t ({stock['SMA_S']}:{stock['SMA_L']})")
    #pass
  else:
    #print(stock)
    print(f"{stock['startdate']}--{stock['enddate']}")