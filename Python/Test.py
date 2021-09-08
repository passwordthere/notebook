url = "https://gmp.wdf.sap.corp/cgi-bin/off_dispatch.pl/edit?id=2021-%s"
strs = ['12345','23456']
print(strs)
for str in strs:
    print(url.replace('%s', str))