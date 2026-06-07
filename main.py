# import login as l
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
data = []

established_year = []
students_served = []
city = []
country_ids = []
university_ids = []
services = []

consultancyAddress, Services = re.getAddressAndServices()
consultancyServiceIds = ServiceId.getIds()



with open("BackUpWithoutAi.json","r") as f:
    data = json.load(f)
    dataLength = len(data)


for i, eachData in enumerate(data):
    logoData = Dl.downloadLogo(eachData["Logo"],eachData["Url"])
    LogodownloadName.insert(i,logoData)
    consultancyName.insert(i,eachData["Name"])
    consultancyUrl.insert(i,eachData["Url"])
    consultancyDesc.insert(i,eachData["Desc"])

    max_len = max(len(LogodownloadName),len(consultancyName),len(consultancyUrl),len(consultancyDesc))

    print(len(LogodownloadName),len(consultancyName),len(consultancyUrl),len(consultancyDesc))

    if (max_len-len(LogodownloadName))>0:
        name += [""]
    if (max_len-len(consultancyName))>0:
        logo += [""]
    if (max_len-len(consultancyUrl))>0:
        ConsultancyDesc += [""]
    if (max_len-len(consultancyDesc))>0:
        url += [""]
    if (max_len-len(established_year))>0:
        url += [0]
    if (max_len-len(students_served))>0:
        url += [0]
    if (max_len-len(city))>0:
        url += [""]
    if (max_len-len(country_ids))>0:
        url += [""]
    if (max_len-len(university_ids))>0:
        url += [""]
    if (max_len-len(services))>0:
        url += [""]
    




dataToPopulate = [
        consultancyName,
        consultancyDesc,
        consultancyUrl,
        LogodownloadName,
        consultancyAddress,
        consultancyServiceIds,
        established_year,
        students_served,
        city,
        country_ids,
        university_ids,
        services

]

IncreasePopulation.populateData(dataToPopulate,dataLength)



