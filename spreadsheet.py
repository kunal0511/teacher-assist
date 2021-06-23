import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Links of sites').sheet1
list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)
websites = []
for i in range(500):
     websites.append(list_of_hashes[i][''])
#print (websites)
 
