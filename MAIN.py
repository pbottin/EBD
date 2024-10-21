# from VSCODE
import pdb
import os, sys, time
import requests

print("FIRST TRY")
print("CREATION DATE: 19/08/24")
print("LAST MODIFICATION DATE: 29/09/24")

## Problems to solve
#  - Delete link no more used
#  - Insert name of the new file ==> save the name after the link separated by some symbols
#  - More file extensions (not only pdf) (geoportali)
#  - Notifiche di caricamento documentazione su sito

## To enter in the .venv ==> Set-ExecutionPolicy Unrestricted -Scope Process ==> .venv\Scripts\activate
## Install requests in .venv ==> pip install requests
## Install pyistaller in .venv
## Create excecutable ==> pyinstaller .\MAIN.py --onefile

def main():

    ################
    ## START PROGRAM
    listPath = "C:\\Windows\\Temp" #"C:\\Users\\PBottin\\Desktop" #

    if len(sys.argv) == 1: ## Doppio click, non vengono dati parametri aggiuntivi ma unico parametro è percorso file
        MODE = "icon"
        Link = str(input("Inserisci il link dei documenti che ti interessano: \n"))
        if len(Link) == 0: ## Se premo solo invio (stringa vuota) funziona come in avvio
            MODE = "start"
            Link = ""
            fileName = ""
            downloadPath = ""
        else: # Se non viene dato il link non viene richiesto altro
            fileName = str(input("Inserisci il nome identificativo del documento: \n"))
            downloadPath = str(input("Inserisci il percorso di download del file: (default C:/Windows/Temp) \n"))

    else: ## Start
        MODE = "start"

    ## Check if the list document is already in the Temp folder
    if "List.txt" not in os.listdir(listPath):
        ## If it's the first time using the code, the list will be created        
        if len(downloadPath) == 0:
            downloadPath = "C:\\Windows\\Temp"
        with open(listPath+"\\List.txt", "w") as file:
            pass
        file.close()

    scriptPath = sys.path[0]

    # fileName = "Documento.pdf"   
    # print('Path of the script: ' + scriptPath)
    # print('Downloading file to: ' + downloadPath)
    if MODE == "icon":
        ## Solo se il link è presente
        ## e, quindi, sono inseriti anche downloadPath
        ## e nome documento
        checkLink(Link, fileName, downloadPath, listPath)
        
    with open(listPath + "\\List.txt", "r") as fileList:
        for line in fileList:
            Split = line.split("$$")
            var = Split[0].strip()
            downloadFile(var, downloadPath, fileName)
            time.sleep(1)

    print('File downloaded...')
    print('Exiting program...')

    return

## FUNCTIONS
def extractName(url):
    '''
    Exctraction of the name of the file from the url link
    '''
    import pdb
    url = url[:-1]
    url = url.replace("%20", "_")
    W = url.index("www")
    B = (url[W+4:]).index("/") ## +4 because it has to delete the "www."
    Sito = (url[W+4:(W+4+B)]).replace(".it", "")
    Split = url.split("/")
    Nome = Sito +"_" +Split[-1]
    return Nome

def downloadFile(url, downloadPath, fileName):
    '''
    Download process for a single file
    '''
    from urllib.request import urlretrieve
    # Nome = extractName(url)
    urlretrieve(url, downloadPath + "\\" + fileName + ".pdf")
    # with open(downloadPath + "\\" + Nome + ".pdf", "wb") as file:
    #     response = requests.get(url)
    #     file.write(response.content)
    # file.close()
    return

def checkLink(url, fileName, downloadPath, listPath):
    '''
    Check for the presence of a lin in the general list
    '''
    ## Check if the link is already in the list
    List = []
    with open(listPath + "\\List.txt", "r") as file:
        for line in file:
            line.split("$$")
            if url != str(line[0].strip()):
                List.append(line)
            else:
                pass           
    file.close()
    ## Adding the link
    List.append(url+" $$ "+fileName+" $$ "+downloadPath)

    ## Rewriting list
    with open(listPath + "\\List.txt", "w") as file:
        for element in List:
            file.write(element)
        file.write("\n")
    file.close()
    return

if __name__ == "__main__":
    main()
