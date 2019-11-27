import urllib.parse, requests

serviceurl = 'https://beta.soldai.com/bill-cipher/askquestion?'
#key='key=ee94a162ec172d2394930d7175be293046338af9'
key='key=b7a496cf65759694b6978962533a5fac3edd0ffe'
serviceurl += key + '&question='  

next = True
counter = 1
while next:
    question = input('Usuario[' + str(counter) + ']:')
    if len(question) < 1 :
        next = False
        continue

    url = serviceurl + urllib.parse.urlencode({'question':question})
    data = requests.get(url).json()
    ans = data["current_response"]["message"]
    #print(data)
    print('Hermes[' + str(counter) + ']:' + ans)
    print('Intent:' +str( data["current_response"]["intent_info"]["id"]) +  " , " + str(data["current_response"]["intent_name"]))
    counter += 1
