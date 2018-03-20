import requests
import requests_cache

requests_cache.install_cache('stack_cache')

url = 'https://api.stackexchange.com/2.2/similar?'

def get_stack_source(title):

    try:
        params = {
        'order': 'desc',
        'sort': 'relevance',
        'title': title,
        'site': 'stackoverflow'
        }

        response = requests.get(url, params).json()

        resp_dict = {}
        i = 0
        while i < 5:
            item = response['items'][i]
            resp_dict.update({('item'+str(i)): {'title': item['title'], 'link': item['link']}})
            i += 1

        return resp_dict

    except Exception as e:
        print('Error ', e)
