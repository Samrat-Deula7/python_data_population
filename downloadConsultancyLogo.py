import requests

def downloadLogo(WebUrl,logoPath,save_as="logo.png"):

    logoUrl = WebUrl.rstrip("/")+"/"+logoPath.lstrip("/")

    try:
        response = requests.get(logoUrl,stream=True,timeout=30)

        response.raise_for_status()

        with open(save_as,"wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        
    except Exception as e:
        print("Couldn't download the logo:",e)