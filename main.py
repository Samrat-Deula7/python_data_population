import login as l
import downloadConsultancyLogo as Dl
import json
import populateConsultancyData as IncreasePopulation
import readExcel as re
from serviceTypeCheck import check
import getServicesId as ServiceId

consultancyName = []
consultancyUrl = []
LogodownloadName = []
consultancyDesc = []

consultancyAddress, Services = re.getAddressAndServices()
consultancyServiceIds = ServiceId.getIds()



with open("BackUpWithoutAi.json","r") as f:
    data = json.load(f)
    dataLength = len(data[0:1])


for i, eachData in enumerate(data[0:1]):
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
        consultancyAddress,
        consultancyServiceIds
]

IncreasePopulation.populateData(l.cookies,dataToPopulate,dataLength)



