import zipfile
import time
folderPath = input("Enter the path to the file: ")
zipf = zipfile.ZipFile(folderPath)
global result
global tried
global c
result = 0
c = 0
tried = 0

if not zipf:           #Checks if the file is password encrypted
    print('The zipped file/folder is not password protected! You can successfully open it!') 
else:
    starttime = time.time()
    wordfile = open("wordlist.txt", "r", errors="ignore")
    body = wordfile.read().lower()
    words = body.split("\n")
    for i in range(len(words)):
        w = words[i]
        c = c+1
        print(w)
        password = w.encode("utf-8").strip()
        try:
            with zipfile.ZipFile(folderPath, "r") as zf:
                zf.extractall(pwd=password)
                print("Sucess! The password is: " + w)
                endtime = time.time()
                result=1
            break
        except:
            pass
duration = endtime - starttime

if result ==0:
    print(f"Password not found. A total of {c} combinations were tried in duration of {duration}. Password is not of 4 characters")
else:
    print(f"Password found while checking {c} combinations in a duration of {duration}")