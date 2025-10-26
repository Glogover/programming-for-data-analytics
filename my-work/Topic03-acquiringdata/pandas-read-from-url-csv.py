# Program showing how to read csv from a url using Pandas
# Author: Marcin Kaminski

import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=52.8436&longitude=-8.9864&daily=temperature_2m_max,temperature_2m_min&format=csv"


# or a different protocol (you will need to pip install S3Fs)
# url = "s3://noaa-gsod-pds/2020/72278023183.csv"

df = pd.read_csv(url)
print(df.head)

