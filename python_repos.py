import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# make a api calls

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

r = requests.get(url)

print("Status code:", r.status_code)

# store the api request into a variable

response_dict = r.json()

# Show the total
print("Total repositories", response_dict['total_count'])

# explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

names,stars = [], []

# make a analysis of repos
for repo_dicts in repo_dicts:
    names.append(repo_dicts['name'])
    stars.append(repo_dicts['stargazers_count'])
    # print("\nSelected information about the first repository:")
    # print("\nNmae:",repo_dicts['name'])
    # print("\nOwner:",repo_dicts['owner']['login'])
    # print("\Stars:",repo_dicts['stargazers_count'])
    # print("\nRepository:",repo_dicts['html_url'])
    # print("\nCreated", repo_dicts['created_at'])
    # print("\nUpdated", repo_dicts['updated_at'])
    # print("\Description:",repo_dicts['description'])

# create the chart bar
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45, show_legend=False)
chart.title= 'Most-Starred Pyhton Projects on GitHub'
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('python_repos.svg')