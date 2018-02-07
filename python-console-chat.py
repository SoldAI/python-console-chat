import urllib
import json

serviceurl = 'http://www.soldai.com/hermes/api/v2/hacerpregunta?'
key='key=f56b11cc51bc8cb9643ebc9139ba45a411b94ac6'
serviceurl += key + '&q='  

next = True
counter = 1
while next:
    question = raw_input('Usuario[' + str(counter) + ']:')
    if len(question) < 1 :
        next = False
        continue

    url = serviceurl + urllib.urlencode({'q':question})

    #print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    #print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None

    #print json.dumps(js, indent=4)

    ans = js["respuesta"]
    print 'Hermes[' + str(counter) + ']:' + ans
    counter += 1
