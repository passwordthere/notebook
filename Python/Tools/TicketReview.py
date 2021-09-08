import webbrowser as w

url = "https://gmp.wdf.sap.corp/cgi-bin/off_dispatch.pl/edit?id=2021-%s"
inputs = input()
keywords = list(map(str, inputs.split()))

for keyword in keywords:
    u = url.replace("%s", keyword)
    w.open(u)