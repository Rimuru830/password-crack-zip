import zipfile

#create object of zipfile to crack
zip_file = zipfile.ZipFile("crack_test_file.zip")

#open wordlist 
with open("password.txt", "rb") as file:
          #read each line
          for line in file:
                  line = line.strip()
                  # try extract zip file
                  try:
                      zip_file.extractall(pwd=line)

                      #if password valid
                      print("password found",line)
                      break
                  except:
                      continue    
