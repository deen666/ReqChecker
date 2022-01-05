import requests

class ChecK():

    def __init__(self):
        self.targeturl = str(input("Enter Target: "))
        self.fwords = str(input("Word to find: "))
        self.target()

    def PrintT(self):
        print(f"{self.fwords} in {self.targeturl} = Found"+"\n")

    def PrintF(self):
        print(f"{self.fwords} in {self.targeturl} = Not Found"+"\n")

    def target(self):
        print("==================")
        print("[+] Target [+]")
        print("")
        url = "https://"+self.targeturl
        r = requests.Session()
        r.headers = {
        'Host': url,
        'Accept': '*/*',
        'Accept-Encoding': '*/*',
        'Origin': url,
        'User-Agent': 'Mozilla/5.0', # Set UA.
        'Connection':'close',
        'Referer': url
        }
        req = r.get(url)
        print(req.text) # If the response is blank.
        print('')
        if req.text.find(self.fwords) >= 0 : # Find somethings.
            self.PrintT()
        else:
            self.PrintF()



if __name__ == "__main__":
    print("""
        ======================================= 
                ~[$] done by DEEN
        =======================================
        """)
    ChecK()


print('')    
print('Press enter to exit .')
input('')
