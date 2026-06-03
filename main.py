import login as l
import downloadConsultancyLogo as Dl
import json
import populateConsultancyData as IncreasePopulation

consultancyName = []
consultancyUrl = []
LogodownloadName = []
consultancyDesc = []


with open("BackUpWithoutAi.json","r") as f:
    data = json.load(f)
    dataLength = len(data[12:13])

for i, eachData in enumerate(data[12:13]):
    logoData = Dl.downloadLogo(eachData["Logo"])
    LogodownloadName.insert(i,logoData)
    consultancyName.insert(i,eachData["Name"])
    consultancyUrl.insert(i,eachData["Url"])
    consultancyDesc.insert(i,eachData["Desc"])
    

dataToPopulate = [
        consultancyName,
        consultancyDesc,
        consultancyUrl,
        LogodownloadName,
]
IncreasePopulation.populateData(l.cookies,dataToPopulate,dataLength)
# l.cookies
# Dl.downloadedName

