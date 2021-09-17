import webbrowser as w

url = "https://gmp.wdf.sap.corp/cgi-bin/search.fpl?search=%s"
doc = "https://bit-twiki.wdf.sap.corp/bin/view/ToolsAndHelper/Processes/HowToPrepareRepaired"
inputs = input("Server: ")
keywords = list(map(str, inputs.split()))

for keyword in keywords:
    u = url.replace("%s", keyword)
    w.open(u)
w.open(doc)
print()
print("- Precheck")
print()
print("- Install")
print()
print("- AdditionalCheck")
print()
print("- LACP")
print()
print("- Status&Comments")
print()
print("- SNOW")
print("Hello colleagues,\n\nThere's no issue occurs after reinstalling.\nKindly close the ticket.\n\nRegards,\nMurphy\n\nGCS-Compute-GMP")
print()
input('Press Enter to exit...')