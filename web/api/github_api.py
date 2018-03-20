import requests
import requests_cache

requests_cache.install_cache('github_cache')

url = 'https://api.github.com/search?q=' + search_term +'&type=Issues&utf8=✓'

def get_stack_source(title):

    try:
        params = {
        'order': 'desc',
        'sort': 'relevance',
        'title': title,
        'site': 'github'
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
