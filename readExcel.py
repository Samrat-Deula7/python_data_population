import pandas as pd

def getAddressAndServices():

    df = pd.read_excel("E:\\Work project\\consultancy_data_updated.xlsx")


    Address = df["Address"].tolist()
    Services = df["Approved Services"].tolist()


    return Address, Services
