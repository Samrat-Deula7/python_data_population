import login as l
import downloadConsultancyLogo as Dl
import json

consultancyName = []
consultancyUrl = []
LogodownloadName = []
consultancyDesc = []


with open("BackUpWithoutAi.json","r") as f:
    data = json.load(f)

for i, eachData in enumerate(data):
    logoData = Dl.downloadLogo(eachData["Logo"])
    LogodownloadName.insert(i,logoData)
    consultancyName.insert(i,eachData["Name"])
    consultancyUrl.insert(i,eachData["Url"])
    consultancyDesc.insert(i,eachData["Desc"])

data = {
        "Name": consultancyName,
        "Url": consultancyUrl,
        "Logo": LogodownloadName,
        "Desc": consultancyDesc
    }

# l.cookies
# Dl.downloadedName

