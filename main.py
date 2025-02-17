import requests
from Valid import Valid

'''
Wi
'''
def main():
  #Get data from an external API
  response = requests.get("http://178.128.144.132/data/")

  #open file to write to
  #store ZIPs and Phones in a local file.
  # format should be a valid ID ZIP PHONE on each line
  out_file = open("results.csv", "w")

  print("Writing JSON to file.")
  for obj in response.json():
    #print(obj)
    
    #TODO: validate before write.
    #Valid module contains static validation method stubs

    #zip is located in obj[3]
    if not Valid.zip(obj[3]):
      continue
    
    #phone is in obj[4]
    if not Valid.phone(obj[4]):
      continue

    line = obj[0] + " " + obj[3] + " " + obj[4] + '\n'

    out_file.write(line)
  
  print("Done.")

  return #end main

if __name__ == '__main__':
  main()