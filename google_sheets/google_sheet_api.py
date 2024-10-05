import gspread_asyncio
from google.oauth2.service_account import Credentials


# First, set up a callback function that fetches our credentials off the disk.
# gspread_asyncio needs this to re-authenticate when credentials expire.
def get_creds():
    # To obtain a service account JSON file, follow these steps:
    # https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account
    creds = Credentials.from_service_account_file("serviceacct_spreadsheet.json")
    scoped = creds.with_scopes([
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])
    return scoped

def get_agcm():
    agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)
    return agcm

agcm = get_agcm()

__all__ = ['agcm']