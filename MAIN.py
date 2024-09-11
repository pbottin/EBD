# from VSCODE
import pdb
import os, sys
import requests

print("FIRST TRY")
print("CREATION DATE: 19/08/24")
print("LAST MODIFICATION DATE: 11/09/24")

## To enter in the .venv ==> Set-ExecutionPolicy Unrestricted -Scope Process ==> .venv\Scripts\activate
## Install requests in .venv ==> pip install requests
## Install pyistaller in .venv
## Create excecutable ==> pyinstaller .\MAIN.py --onefile

## FUNCTIONS
def downloadFile(url, downloadPath, fileName):
    ## Download funtion
    from datetime import datetime
    
    info = datetime.today().strftime('%Y-%m-%d_%H_%M_%S')
    with open(downloadPath + "\\" + (fileName.replace('.pdf', '')) + "_" + str(info) + ".pdf", "wb") as file:
        response = requests.get(url)
        file.write(response.content)
    file.close()

    return

def checkLink(url, listPath):
    ## Check if the link is already in the list
    List = []
    with open(listPath + "\\List.txt", "r") as file:
        for line in file:
            if url != str(line.strip()):
                Li%st.append(line)
            else:
                pass           
    file.close()
    ## Adding the link
    List.append(url)

    ## Rewriting list
    with open(listPath + "\\List.txt", "w") as file:
        for element in List:
            file.write(element)
        file.write("\n")
    file.close()
    return

## START LOGIC PART
# print(sys.argv[0])

listPath = "C:\Windows\Temp" #C:\\Users\\PBottin\\Desktop"
downloadPath = "C:\Windows\Temp" #"C:\\Users\\PBottin\\Desktop"

if len(sys.argv) == 1: ## Doppio click, non vengono dati parametri aggiuntivi ma unico parametro è percorso file
    MODE = "icon"
    Link = str(input("Inserisci il link dei documenti che ti interessano: \n"))
    if len(Link) == 0: ## Se premo solo invio (stringa vuota) funziona come in avvio
        MODE = "start"
else: ## Start
    MODE = "start"


## Check if the list document is already in the Temp folder
if "List.txt" not in os.listdir(listPath):
    ## If it's the first time using the code, the list will be created
    with open(listPath, "w") as file:
        pass
    file.close()

scriptPath = sys.path[0]

fileName = "Prova.pdf"     
print('Path of the script: ' + scriptPath)
print('Downloading file to: ' + downloadPath)
if MODE == "icon":
    checkLink(Link, listPath)
    
with open(listPath + "\\List.txt", "r") as fileList:
    for line in fileList:
        downloadFile(line, downloadPath, fileName)

print('File downloaded...')
print('Exiting program...')
