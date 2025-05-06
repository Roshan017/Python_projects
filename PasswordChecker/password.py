import requests
import hashlib 

def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching: {res.status_code}')
    return res



def get_pwd_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in  hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0 




def pwned_api_check(passwrd):
    sha1pwd = hashlib.sha1(passwrd.encode('utf-8')).hexdigest().upper()
    five_char , tail = sha1pwd[:5],sha1pwd[5:]
    resp = request_api_data(five_char)
    #print(resp)
    return get_pwd_leak_count(resp,tail)


def main():
    try:
        with open("P.txt", mode="r", encoding='utf-8') as pw:
            password = pw.readline()
    except FileExistsError:
        print("File Not Found")
   

    count2 = pwned_api_check(password)
    count1 = int(count2)
    print(count1)

    if count1==0:
        print("Looks good, Its a unique Password")
    elif count1>10 and count1 < 20:
        print("Its okay,But not unique")
    elif count1>20 and count1 < 40:
        print("Maybe Change It, Similar passwords were found")
    elif count1>40 and count1 < 50:
        print("Better Change it")
    elif count1>50:
        print("Weak Password")

    
    
    print("Checked")
    


main()