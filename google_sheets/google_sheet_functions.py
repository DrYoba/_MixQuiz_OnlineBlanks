from typing import Dict
from google_sheets.google_sheet_api import agcm


async def authorize():
    agc = await agcm.authorize()
    return agc

async def next_available_row(worksheet):
    str_list = list(filter(None, await worksheet.col_values(8)))
    return str(len(str_list)+1)

async def push_data(data: Dict[str, str]):
    agc = await authorize()
    ss = await agc.open("MAIN")
    ws = await ss.get_worksheet(0)

    row = await next_available_row(ws)

    cells = await ws.range('%s:%s' % (f"A{row}", f"M{row}"))

    cells[0].value = data["answer1"]
    cells[1].value = data["answer2"]
    cells[2].value = data["answer3"]
    cells[3].value = data["answer4"]
    cells[4].value = data["answer5"]
    cells[5].value = data["answer6"]
    cells[6].value = data["answer7"]
    cells[7].value = data["team"]
    cells[8].value = data["referer"]
    cells[9].value = data["formid"]
    cells[10].value = f'round{data["Form name"][-1]}'
    cells[11].value = data["sent"]
    cells[12].value = data["requestid"]

    await ws.update_cells(cells)
    print("All done!")