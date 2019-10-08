import scraper
import get_urls
import pprint
import pymongo

def ins(collName,doc):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['events']
    coll = db[collName]
    if len(doc)>1:
        ids = coll.insert_many(doc)
        print(ids.inserted_ids)
    else:
        ids=coll.insert_one(doc)
        print(ids)
def get_resp_list(urls):
    res = []
    l=len(urls)
    if(l<10):
        max=l
    else:
        max=10
    for url in urls[:max]:
        print('scraping '+url)
        res.append(scraper.parse_from_url(url)[0])
    s=urls[0]
    start=s.find('//')+len('//')
    domain=s[start:s[start:].find('/')+start]
    domain=domain.replace('.','_')
    print(domain)
    ins('interesting_urls',dict({domain:urls[:max]}))
    ins("non_interesting_urls",dict({domain:urls[max:]}))
    return res

def events_high():
    res=scraper.parse_from_url("https://www.eventshigh.com/mumbai/classes+and+workshops?src=cityPage&filterDate=")
    return res
    # pprint.pprint(res[0])
    # print(len(res))

def naadyoga():
    urls = get_urls.get("https://naadyogacouncil.com/")
    res=get_resp_list(urls)
    #pprint.pprint(res)
    #print(len(res))
    return res

def insider():
    urls=get_urls.get_in("https://insider.in/all-workshops-in-mumbai/")
    print('fetched urls..')
    res=get_resp_list(urls)
    print(len(res))
    return res

res=insider()
#ins('insider',res)
#res=events_high()
#print(res[0])
# ins('eventshigh',res)
res=naadyoga()
#print(res[0])
#ins('naadyoga',res)