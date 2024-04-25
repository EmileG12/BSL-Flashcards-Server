import urllib.request

print(urllib.request.urlopen("http://127.0.0.1:8000/decklist").read())
contents = urllib.request.urlopen("http://127.0.0.1:8000/decklist").readlines()
for i in contents:
    print(i)


