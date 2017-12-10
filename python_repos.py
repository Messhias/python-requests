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

names,plot_dicts = [], []

# make a analysis of repos
for repo_dicts in repo_dicts:
    plot_dict ={
        'value': repo_dicts['stargazers_count'],
        'label': repo_dicts['name'],
        'xlink': repo_dicts['html_url']
    }
    plot_dicts.append(plot_dict)
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

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title= 'Most-Starred Pyhton Projects on GitHub'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')