from flask import Flask, render_template
from dateutil import parser
from operator import itemgetter
import requests, json

application = Flask(__name__)

# search_term is a given term to search Github repositories
@application.route('/navigate/<search_term>')
def navigate(search_term):
  # The Github api keyword "q" helps searching for repositories with the word "search_term"
  gitrepo_search = "https://api.github.com/search?q=" + search_term +"&type=Issues&utf8=✓"

  github_repo = requests.get(gitrepo_search)
  git_info = github_repo.read()
  data = json.loads(git_info)
  count = 0;
  information = []

  #Github repository information
  for result in data["items"]:
   name = data['items'][count]['owner']['login']
   html_url = data['items'][count]['owner']['html_url']
   issues = data['items'][count]['issues']

   information.append((name, fix_datetime(created_at), html_url, avatar_url, repo, commiturl))
   count=count+1
   #print count
  # Rendering template.html with a sorted repo information
  return render_template('template.html', name = sortrepos(information))

# Fixing datetime format
def fix_datetime(date):
  lis = list(date)
  lis[19:20]=''
  created_at = "".join(lis)
  created_at = created_at.replace("T"," ")
  created_time = parser.parse(created_at)
  return created_time

# Sorting repositories in descending order
def sortrepos(info):
  repo = sorted(info, key=itemgetter(1),  reverse=True) # Sorting by creation date(key: 1) in descending order
  max = 5 # The first 5 newest items
  repos = []

  for index in range(len(repo)):
   if index < max:
     an_item = dict(owner=repo[index][0], created_at=repo[index][1], git_url=repo[index][2], avatar_url=repo[index][3],repo=repo[index][4], comm=latestcommit(repo[index][5]))
     repos.append(an_item)
     print(info[index][1]), repo[index][0], repo[index][1], repo[index][2], repo[index][3], repo[index][4]
  return repos

if __name__ == "__main__":
    application.run(host='0.0.0.0')
