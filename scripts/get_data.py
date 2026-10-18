"""Download the Hillstrom MineThatData email experiment CSV to data/raw/."""
from pathlib import Path
from urllib.request import urlretrieve

URL = ("http://www.minethatdata.com/"
       "Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv")
OUT = Path(__file__).resolve().parent.parent / "data" / "raw" / "hillstrom.csv"

if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    urlretrieve(URL, OUT)
    print(f"saved {OUT}")
