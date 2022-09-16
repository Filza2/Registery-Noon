try:from requests import post
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()
print("""
██████╗ ███████╗ ██████╗       ███╗   ██╗ ██████╗  ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔════╝       ████╗  ██║██╔═══██╗██╔═══██╗████╗  ██║
██████╔╝█████╗  ██║  ███╗█████╗██╔██╗ ██║██║   ██║██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝  ██║   ██║╚════╝██║╚██╗██║██║   ██║██║   ██║██║╚██╗██║
██║  ██║███████╗╚██████╔╝      ██║ ╚████║╚██████╔╝╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝ ╚═════╝       ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══
                             
                  By @TweakPY - @vv1ck
""")
email=input("{?} Email : ");fn=input("{?} First Name : ");ln=input("{?} Last Name : ");pess=input("{?} Password : ")
rq=post('https://login.noon.com/_svc/customer-v1/customer',headers={'Host': 'login.noon.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/plain, */*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://login.noon.com/saudi-ar/signup','Content-Type': 'application/json','Cache-Control': 'no-cache','X-Locale': 'en-sa','X-Platform': 'web','Content-Length': '104','Origin': 'https://login.noon.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'},json={"email":email,"password":pess,"firstName":fn,"lastName":ln})
if 'firstName' in rq.text:print('\n- Succeeded');print(f"[+] Join Date: [{rq.json()['data']['joinDate']}]\n[+] Subscription Key: [{rq.json()['data']['subscriptionKey']}]\n\n")
elif 'error' in rq.text:print(f"- Failed : {rq.json()['error']}")
else:print('\n- Error')
