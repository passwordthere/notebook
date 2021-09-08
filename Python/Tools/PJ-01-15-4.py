import webbrowser as w

url = "https://gmp.wdf.sap.corp/cgi-bin/dnsmanager.pl/host/?sub=hostmask&action=edit&objid=%s"
inputs = input()
keywords = list(map(str, inputs.split()))

for keyword in keywords:
    u = url.replace("%s", keyword)
    w.open(u)