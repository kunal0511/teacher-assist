from datetime import *
from time import *
from spreadsheet import websites

def block():
    host_path = r"C:\Windows\System32\drivers\etc\hosts" 
    redirect = "127.0.0.1"  
    print(websites)
    while True:  
            with open(host_path,"r+") as fileptr:  
                content = fileptr.read()  
                for website in websites:  
                    if website in content:
                        print("Pass")
                        pass  
                    else:  
                        fileptr.write(redirect+"        "+website+"\n")
                        print("Websites Blocked!")
                break


def unblock():
    host_path = r"C:\Windows\System32\drivers\etc\hosts" 
    redirect = "127.0.0.1"  
    print("Time over")
    with open(host_path,'r+') as file:  
        content = file.readlines();  
        file.seek(0)  
        for line in content:  
            if not any(website in line for website in websites):  
                file.write(line)  
            file.truncate()


