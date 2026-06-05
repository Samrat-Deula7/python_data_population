import login as l
import downloadConsultancyLogo as Dl
import json
import populateConsultancyData as IncreasePopulation
import readExcel as re
import serviceTypeCheck 

consultancyName = []
consultancyUrl = []
LogodownloadName = []
consultancyDesc = []
servicesId = []

consultancyAddress, Services = re.getAddressAndServices()


# Services_Data_Ids = {
#     "Guidance for study destinations abroad": 272,
#     "Intensive training for IELTS exam success": 273,
#     "Focused preparation for TOEFL test takers": 274,
#     "Coaching for GRE analytical and verbal skills": 275,
#     "Preparation for GMAT business school entry": 276,
#     "Exam readiness for SAT college admissions": 277,
#     "Practice sessions for PTE language test": 278,
#     "Coaching for medical entrance examinations": 279,
#     "Preparation for public service commission exams": 280,
#     "Exam prep for nursing entrance tests": 281,
#     "Preparation for MBA entrance examinations": 282,
#     "Bridge course for academic transition support": 283,
#     "Focused training for CMAT management test": 284,
#     "Preparation for KUMAT university entrance exam": 285,
#     "Coaching for ACCA professional qualification": 286,
#     "Exam prep for GNK specialized tests": 287,
#     "Subject-specific coaching in Botany": 288,
#     "Subject-specific coaching in Physics": 289,
#     "Subject-specific coaching in Mathematics": 290,
#     "Training for general standardized exams": 291,
#     "Learn Japanese for study and work": 292,
#     "Master English for global communication": 293,
#     "Learn German for academic and career growth": 294,
#     "Learn Korean for cultural and professional use": 295,
#     "Learn French for international opportunities": 296,
#     "Learn Chinese for business and education": 297,
#     "Learn Spanish for global communication": 298,
#     "Learn Hebrew for cultural and academic purposes": 299
# }



with open("BackUpWithoutAi.json","r") as f:
    data = json.load(f)
    dataLength = len(data[16:17])


for i, eachData in enumerate(data[16:17]):
    # logoData = Dl.downloadLogo(eachData["Logo"])
    # LogodownloadName.insert(i,logoData)
    consultancyName.insert(i,eachData["Name"])
    consultancyUrl.insert(i,eachData["Url"])
    consultancyDesc.insert(i,eachData["Desc"])

    filteredServices = Services[i].split("|")
    
   

  
    

    if len(filteredServices) < 2:
        service1 = filteredServices[0].split(",")
        # servicesId.insert(i,serviceTypeCheck.check(service1[1]))
        serId1 = serviceTypeCheck.check(service1[1])
        print(service1[1])
    elif len(filteredServices) == 2:
        service1 = filteredServices[0].split(",")
        service2 = filteredServices[1].split(",")
        # servicesId.insert(i,serviceTypeCheck.check(service1[1])+","+serviceTypeCheck.check(service2[1]))
        serId1 = serviceTypeCheck.check(str(service1[1]))
        serId2 = serviceTypeCheck.check(str(service2[1]))
        print(serId1)
        print(serId2)
        print(service1[1],service2[1])
    else:
        service1 = filteredServices[0].split(",")
        service2 = filteredServices[1].split(",")
        service3 = filteredServices[2].split(",")
        # servicesId.insert(i,serviceTypeCheck.check(service1[1])+","+serviceTypeCheck.check(service2[1])+","+serviceTypeCheck.check(service3[1]))
        print(service1[1],service2[1],service3[1])

    print(servicesId)
    # consultancyServices.insert(i,servicesObjArr)


# dataToPopulate = [
#         consultancyName,
#         consultancyDesc,
#         consultancyUrl,
#         LogodownloadName,
#         consultancyAddress,
#         consultancyServices
# ]
# IncreasePopulation.populateData(l.cookies,dataToPopulate,dataLength)



