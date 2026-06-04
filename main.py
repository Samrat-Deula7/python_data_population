import login as l
import downloadConsultancyLogo as Dl
import json
import populateConsultancyData as IncreasePopulation
import readExcel as re

consultancyName = []
consultancyUrl = []
LogodownloadName = []
consultancyDesc = []
consultancyServices = []

consultancyAddress, Services = re.getAddressAndServices()

# print("????????????????????????")
# print(consultancyAddress)
# print(Services)
# print("????????????????????????")



with open("BackUpWithoutAi.json","r") as f:
    data = json.load(f)
    dataLength = len(data[16:17])

# print(consultancyServices)

for i, eachData in enumerate(data[16:17]):
    logoData = Dl.downloadLogo(eachData["Logo"])
    LogodownloadName.insert(i,logoData)
    consultancyName.insert(i,eachData["Name"])
    consultancyUrl.insert(i,eachData["Url"])
    consultancyDesc.insert(i,eachData["Desc"])

    filteredServices = Services[i].split("|")
    service1 = filteredServices[0].split(",")
    service2 = filteredServices[1].split(",")

    objService1 = {
        "title":service1[0],
        "short_text":service1[1],
        "icon":service1[2]
    }
    objService2 = {
        "title":service2[0],
        "short_text":service2[1],
        "icon":service2[2]
    }

    servicesObjArr = json.dumps([objService1,objService2])
    consultancyServices.insert(i,servicesObjArr)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@222")
# print(consultancyServices)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

dataToPopulate = [
        consultancyName,
        consultancyDesc,
        consultancyUrl,
        LogodownloadName,
        consultancyAddress,
        consultancyServices
]
IncreasePopulation.populateData(l.cookies,dataToPopulate,dataLength)



