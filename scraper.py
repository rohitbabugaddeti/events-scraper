import requests
import extruct
headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

#method to check status of url
def is_url_ok(url):
    try:
        return 200 == requests.head(url).status_code
    except Exception:
        return False

def clean_data(data):
    out=[]
    if data['json-ld']!=[]:
        for rec in data['json-ld']:
            try:
                if rec['@type'] == 'Event':
                    d = rec.copy()
                    out.append(d)
            except KeyError:
                pass

    if data['microdata'] != []:
        for rec in data['microdata']:
            try:
                if rec['type'] in ('http://schema.org/Event',
                                   'https://schema.org/Event'):
                    d = rec['properties'].copy()
                    # @context and @type to match json-ld style
                    if rec['type'][:6] == 'https:':
                        d['@context'] = 'https://schema.org'
                    else:
                        d['@context'] = 'http://schema.org'
                    d['@type'] = 'Event'

                    for key in d.keys():
                        if isinstance(d[key], dict) and 'type' in d[key]:
                            type_ = d[key].pop('type')
                            d[key]['@type'] = type_.split('/')[3]  # taking last part of url which holds type

                    out.append(d)
            except KeyError as ke:
                print("Exception :",ke)

    return out

def parse_from_url(url):
    if not isinstance(url,str):
        raise TypeError
    good_data={}
    if(is_url_ok(url)):
        response = requests.get(url, headers=headers)
        data = extruct.extract(response.text, response.url)
        good_data=clean_data(data)
    else:
        print('URL may be Dead/Not Working !')

    return good_data