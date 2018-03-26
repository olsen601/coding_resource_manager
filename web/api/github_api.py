import requests
import requests_cache
import logging

requests_cache.install_cache('github_cache')

url = 'https://api.github.com/search/issues?'

def get_git_source(search_term):

    try:
        params = {
        'q': search_term,
        'type': 'issue'
        }

        response = requests.get(url, params).json()
        logging.info('github API call started')

        resp_dict = {}
        i = 0
        while i < 5:
            item = response['items'][i]
            resp_dict.update({('item'+str(i)): {'title': item['title'], 'link': item['html_url']}})
            i += 1

        return resp_dict

    except Exception as e:
        print('Error ', e)
        logging.info('github exception caught')
