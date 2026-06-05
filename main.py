import login as l
import downloadConsultancyLogo as Dl
import json
import populateConsultancyData as IncreasePopulation
import readExcel as re
from serviceTypeCheck import check

consultancyName = []
consultancyUrl = []
LogodownloadName = []
consultancyDesc = []
servicesId = []

consultancyAddress, Services = re.getAddressAndServices()



with open("BackUpWithoutAi.json","r") as f:
    data = json.load(f)
    dataLength = len(data[16:17])


for i, eachData in enumerate(data[16:17]):
    logoData = Dl.downloadLogo(eachData["Logo"])
    LogodownloadName.insert(i,logoData)
    consultancyName.insert(i,eachData["Name"])
    consultancyUrl.insert(i,eachData["Url"])
    consultancyDesc.insert(i,eachData["Desc"])

    filteredServices = Services[i].split("|")
    
   

  
    

    if len(filteredServices) < 2:
        service1 = filteredServices[0].split(",")
        serId1 = check(service1[1])
        servicesId.insert(i,serId1)
        print(service1[1])
    elif len(filteredServices) == 2:
        service1 = filteredServices[0].split(",")
        service2 = filteredServices[1].split(",")
        serId1 = check(str(service1[1]))
        serId2 = check(str(service2[1]))
        servicesId.append(serId1)
        servicesId.append(serId2)
    else:
        service1 = filteredServices[0].split(",")
        service2 = filteredServices[1].split(",")
        service3 = filteredServices[2].split(",")
        serId1 = check(str(service1[1]))
        serId2 = check(str(service2[1]))
        serId3 = check(str(service3[1]))
        servicesId.append(serId1)
        servicesId.append(serId2)
        servicesId.append(serId3)
        print(service1[1],service2[1],service3[1])

    print(servicesId)


dataToPopulate = [
        consultancyName,
        consultancyDesc,
        consultancyUrl,
        LogodownloadName,
        consultancyAddress,
        servicesId
]
IncreasePopulation.populateData(l.cookies,dataToPopulate,dataLength)



