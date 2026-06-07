import requests

try:
    # url = "http://localhost:5000/api/auth/login"
    # payload = {"username":"admin", "password":"admin"}
    # headers = {
    #     "User-Agent": (
    #         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    #         "AppleWebKit/537.36 (KHTML, like Gecko) "
    #         "Chrome/114.0 Safari/537.36"
    #     )
    # }

    # response = requests.post(url,json=payload,headers=headers,timeout=30)

    # response.raise_for_status()

    # cookies = response.cookies

except Exception as e:
    print("Couldn't logged in",e)