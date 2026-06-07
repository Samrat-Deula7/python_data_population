# import login as l
import downloadConsultancyLogo as Dl
import json
import populateConsultancyData as IncreasePopulation
import readExcel as re
from serviceTypeCheck import check
import getServicesId as ServiceId

consultancies = []

consultancyAddress, Services = re.getAddressAndServices()
consultancyServiceIds = ServiceId.getIds()



with open("BackUpWithoutAi.json","r") as f:
    data = json.load(f)
    dataLength = len(data)


for i, eachData in enumerate(data):
    logoData = Dl.downloadLogo(eachData["Logo"], eachData["Url"])

    consultancies.append({
        "name": eachData["Name"],
        "url": eachData["Url"],
        "desc": eachData["Desc"],
        "logo": logoData,
        "address": consultancyAddress[i],
        "serviceIds": consultancyServiceIds[i],
        "established_year": 0,
        "students_served": 0,
        "city": "",
        "country_id": "",
        "university_id": "",
        "services": ""
    })
    print(len(consultancies))

    IncreasePopulation.populateData(consultancies, len(consultancies))



