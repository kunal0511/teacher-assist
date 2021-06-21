  
import webbrowser
import sys
from datetime import *
from time import *
 

def block():
    host_path = r"C:\Windows\System32\drivers\etc\hosts" 
    redirect = "127.0.0.1"  
    websites = ["www.facebook.com", "www.youtube.com"]
    while True:  
        if datetime(datetime.now().year,datetime.now().month,datetime.now().day,8)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,20):  
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
                break    
        else:  
            with open(host_path,'r+') as file:  
                content = file.readlines();  
                file.seek(0)  
                for line in content:  
                    if not any(website in line for website in websites):  
                        file.write(line)  
                file.truncate()
        sleep(5)  

