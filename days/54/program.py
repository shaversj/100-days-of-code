import requests
import pygal

URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'


r = requests.get(URL)

response = r.json()
print("Total Repositories:", response['total_count'])

names = []
stars = []

data = response['items']

for repos in data:
    names.append(repos['name'])
    stars.append(repos['stargazers_count'])

my_style = pygal.style.LightenStyle(
    '#333366', base_style=pygal.style.LightColorizedStyle)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')
