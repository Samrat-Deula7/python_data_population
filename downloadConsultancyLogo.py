import requests
import shutil
import os

def downloadLogo(logoPath):
    folder = "logos"
    save=logoPath.split("/")[-1]
    save_as=os.path.join(folder,save.split(".")[0]+".png")
    downloadedName = ""


    try:
        if "https://" in logoPath:
            response = requests.get(logoPath,stream=True,timeout=60)

            response.raise_for_status()

            response.raw.decode_content = True

            with open(save_as,"wb") as f:
                shutil.copyfileobj(response.raw,f)
            downloadedName = save_as
            return downloadedName
        else:
            print("Logo not found")
            downloadedName = ""
            return downloadedName

    except Exception as e:
        print("Couldn't download the logo:",e)

