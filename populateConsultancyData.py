import requests
# import downloadConsultancyLogo 

# downloadConsultancyLogo.save_as

try:
    def populateData(cookies,data,dataLength):
        url="http://localhost:5000/api/consultancies"
        payload=""
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0 Safari/537.36"
            )
        }

        print("############################3")
        print(data[5])
        print("#############################3")

        for i in range(dataLength):
            payload = {
                "name": data[0][i],
                "short_bio": data[1][i],
                "long_bio": data[1][i],
                "website": data[2][i],
                "established_year":0,
                "students_served":0,
                "address":data[4][i],
                "city":"",
                "country_ids":'',
                "university_ids":'',
                "services":data[5][i],
                "service_ids":'',
            }
            # print(payload)
            if(open(data[3][i], 'rb') != ""):

                files = {
                    "consultancy_logo": (data[3][i],open(data[3][i], "rb"),"image/png")
                }
                # print(files)
                response = requests.post(url,files=files,data=payload,headers=headers,cookies=cookies,timeout=30)

                response.raise_for_status()
            
            else:
                response = requests.post(url,json=payload,headers=headers,cookies=cookies,timeout=30)

                response.raise_for_status()


    
except Exception as e:
    print("Couldn't populate consultancy data",e)