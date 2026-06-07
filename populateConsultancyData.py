import requests
import pandas as pd



try:
    def populateData(data,dataLength):
       
        print("#####################333")
        print(data[5])
      

        for i in range(dataLength):
            payload = {
                "name": data[0],
                "short_bio": data[1],
                "long_bio": data[1],
                "website": data[2],
                "established_year":data[6],
                "students_served":data[7],
                "address":data[4],
                "city":data[8],
                "country_ids":data[9],
                "university_ids":data[10],
                "services":data[11],
                "service_ids":data[5],
                "logoName":data[3]
            }
          
            df = pd.DataFrame(payload)

            df.to_json("DataToPopulate.json",orient="records",indent=4)



    
except Exception as e:
    print("Couldn't populate consultancy data",e)