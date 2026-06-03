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

dataToPopulate = {
        "Name": consultancyName,
        "Url": consultancyUrl,
        "Logo": LogodownloadName,
        "Desc": consultancyDesc
    }
print(dataToPopulate)
# l.cookies
# Dl.downloadedName

