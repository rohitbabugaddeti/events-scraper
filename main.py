import scraper
import get_urls
import rq_html
import pprint
import pymongo

def ins(collName,doc):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['events']
    coll = db[collName]
    ids = coll.insert_many(doc)
    print(ids.inserted_ids)

def events_high():
    res=scraper.parse_from_url("https://www.eventshigh.com/mumbai/classes+and+workshops?src=cityPage&filterDate=")
    return res
    # pprint.pprint(res[0])
    # print(len(res))

def naadyoga():
    urls = get_urls.get("https://naadyogacouncil.com/")
    res=[]
    for url in urls:
        res.append(scraper.parse_from_url(url)[0])
    pprint.pprint(res)
    return res

def insider():
    pprint.pprint(rq_html.get("https://insider.in/all-workshops-in-mumbai"))

#insider()
res=events_high()
#print(res[0])
# ins('eventshigh',res)
res=naadyoga()
#print(res[0])
#ins('naadyoga',res)