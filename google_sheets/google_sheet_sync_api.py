import gspread

from google_sheets.google_sheet_sync_functions import GoogleSheetManager

gc = gspread.service_account("serviceacct_spreadsheet.json")

gm = GoogleSheetManager(gc)

__all__ = ['gm']
