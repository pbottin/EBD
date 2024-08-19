# from VSCODE
import pdb
import os, sys
from pathlib import Path
import requests

print("FIRST TRY")
print("CREATION DATE: 19/08/24")
print("LAST MODIFICATION DATE: 19/08/24")

Link = str(input("Inserisci il link dei documenti che ti interessano: \n"))
if "List.txt" not in os.listdir("C:\Windows\Temp"):
    with open("C:\\Windows\\Temp\\List.txt", "w") as file:
        pass
    file.close()
else:
    with open("C:\\Windows\\Temp\\List.txt", "w") as file:
        file.write(Link)
    file.close()

def downloadFile(url, downloadPath, fileName):
    from datetime import datetime
    info = datetime.today().strftime('%Y-%m-%d_%H_%M_%S')
    with open(downloadPath + "\\" + (fileName.replace('.pdf', '')) + "_" + str(info) + ".pdf", "wb") as file:
        response = requests.get(url)
        file.write(response.content)

    return

def checkLink(url, listPath):
    ## Check if the link is already in the list
    with open(listPath + "\\List.txt", "a") as file:
        for line in listPath + "\\List.txt":
            if url != str(line):
                file.write(url)
            else:
                pass      
    file.close()
    return

scriptPath = sys.path[0]
listPath = "C:\Windows\Temp"
downloadPath = "C:\\Users\\PBottin\\Desktop"
fileName = "Prova.pdf"     
print('Path of the script: ' + scriptPath)
print('Downloading file to: ' + downloadPath)
checkLink(Link, listPath)
downloadFile(Link, downloadPath, fileName)
print('File downloaded...')
print('Exiting program...')

pdb.set_trace()