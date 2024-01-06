import requests

resp = requests.get("https://e.pcloud.link/publink/show?code=XZ5zS1ZALJkF5xYJn5SgYL9a37Juy2MvjrX")
text = resp.text
n = '"downloadlink": "'
p = text.find(n)
text = text[p + len(n):]
p = text.find('",')
text = text[:p]
text = text.replace('\\', '')
print(text)