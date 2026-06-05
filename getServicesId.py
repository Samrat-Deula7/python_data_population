import readExcel as re
from serviceTypeCheck import check

consultancyAddress, Services = re.getAddressAndServices()



def getIds():
    consultancyServiceIds = []
    servicesId = []

    for i , service in enumerate(Services):

        if "|" in service:

            filteredServices = service.split("|")
        else:
            filteredServices = service

        if len(filteredServices) < 2:
            service1 = filteredServices[0].split(",")
            serId1 = check(str(service1[1]))
            servicesId.insert(i,serId1)
            consultancyServiceIds.insert(i,servicesId)
            servicesId = []
        elif len(filteredServices) == 2:
            service1 = filteredServices[0].split(",")
            service2 = filteredServices[1].split(",")
            serId1 = check(str(service1[1]))
            serId2 = check(str(service2[1]))
            servicesId.append(serId1)
            servicesId.append(serId2)
            consultancyServiceIds.insert(i,servicesId)
            servicesId = []
        elif len(filteredServices) == 3:
            service1 = filteredServices[0].split(",")
            service2 = filteredServices[1].split(",")
            service3 = filteredServices[2].split(",")
            serId1 = check(str(service1[1]))
            serId2 = check(str(service2[1]))
            serId3 = check(str(service3[1]))
            servicesId.append(serId1)
            servicesId.append(serId2)
            servicesId.append(serId3)
            consultancyServiceIds.insert(i,servicesId)
            servicesId = []
        elif len(filteredServices) == 4:
            service1 = filteredServices[0].split(",")
            service2 = filteredServices[1].split(",")
            service3 = filteredServices[2].split(",")
            service4 = filteredServices[3].split(",")
            serId1 = check(str(service1[1]))
            serId2 = check(str(service2[1]))
            serId3 = check(str(service3[1]))
            serId4 = check(str(service4[1]))
            servicesId.append(serId1)
            servicesId.append(serId2)
            servicesId.append(serId3)
            servicesId.append(serId4)
            consultancyServiceIds.insert(i,servicesId)
            servicesId = []
        elif len(filteredServices) == 5:
            service1 = filteredServices[0].split(",")
            service2 = filteredServices[1].split(",")
            service3 = filteredServices[2].split(",")
            service4 = filteredServices[3].split(",")
            service5 = filteredServices[4].split(",")
            serId1 = check(str(service1[1]))
            serId2 = check(str(service2[1]))
            serId3 = check(str(service3[1]))
            serId4 = check(str(service4[1]))
            serId5 = check(str(service5[1]))
            servicesId.append(serId1)
            servicesId.append(serId2)
            servicesId.append(serId3)
            servicesId.append(serId4)
            servicesId.append(serId5)
            consultancyServiceIds.insert(i,servicesId)
            servicesId = []
        elif len(filteredServices) == 6:
            service1 = filteredServices[0].split(",")
            service2 = filteredServices[1].split(",")
            service3 = filteredServices[2].split(",")
            service4 = filteredServices[3].split(",")
            service5 = filteredServices[4].split(",")
            service6 = filteredServices[5].split(",")
            serId1 = check(str(service1[1]))
            serId2 = check(str(service2[1]))
            serId3 = check(str(service3[1]))
            serId4 = check(str(service4[1]))
            serId5 = check(str(service5[1]))
            serId6 = check(str(service6[1]))
            servicesId.append(serId1)
            servicesId.append(serId2)
            servicesId.append(serId3)
            servicesId.append(serId4)
            servicesId.append(serId5)
            servicesId.append(serId6)
            consultancyServiceIds.insert(i,servicesId)
            servicesId = []
        

    return consultancyServiceIds
