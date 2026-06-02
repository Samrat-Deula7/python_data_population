import requests
import shutil

def downloadLogo(logoPath):
    save=logoPath.split("/")[-1]
    save_as=save.split(".")[0]+".png"


    try:
        response = requests.get(logoPath,stream=True,timeout=30)

        response.raise_for_status()

        response.raw.decode_content = True

        with open(save_as,"wb") as f:
            shutil.copyfileobj(response.raw,f)

    except Exception as e:
        print("Couldn't download the logo:",e)

downloadLogo("https://meyvn.edu.np/default/favicon.png")