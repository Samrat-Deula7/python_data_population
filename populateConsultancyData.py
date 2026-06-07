import requests
import pandas as pd



try:
    def populateData(data,dataLength):
        all_payloads = []

        for eachData in data:

            payload = {
                "name": eachData["name"],
                "short_bio": eachData["desc"],
                "long_bio": eachData["desc"],
                "website": eachData["url"],
                "established_year":eachData["established_year"],
                "students_served":eachData["students_served"],
                "address":eachData["address"],
                "city":eachData["city"],
                "country_ids":eachData["country_id"],
                "university_ids":eachData["university_id"],
                "services":eachData['services'],
                "service_ids":eachData["serviceIds"],
                "logoName":eachData["logo"]
            }
            all_payloads.append(payload)
            
        df = pd.DataFrame(all_payloads)

        df.to_json("DataToPopulate.json",orient="records",indent=4)



    
except Exception as e:
    print("Couldn't populate consultancy data",e)