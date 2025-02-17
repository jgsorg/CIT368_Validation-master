import requests
from Valid import Valid

'''
Wi
'''
def main():
  #Get data from an external API
  response = requests.get("http://178.128.144.132/data/")

  if response.status_code != 200: # testing to see if i am getting the data
    print("failed to get data")
    return
  
  data = response.json()
  header = data[0]

  with open("results.csv", "w", encoding="utf-8") as out_file: # added utf8 because google says it will help with encoding issues
    out_file.write(f"{header}\n")

    for obj in data[1:]:
      #proper # of fields
      if len(obj) < 5:
        out_file.write(f"invalid entry, not enough fields: {obj}\n")
        continue

      #zip validation
      if not Valid.zip(obj[3]):
        out_file.write(f"invalid ZIP: {obj[3]}\n")
        continue

      #phone validation
      if not Valid.phone(obj[4]):
        out_file.write(f"invalid phone: + {obj[4]}\n")
        continue

      # valid entry
      line = obj[0] + " " + obj[3] + " " + obj[4] + '\n'
      out_file.write(line)
    
    out_file.write("done")

if __name__ == '__main__':
  main()