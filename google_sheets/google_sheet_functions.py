"""from typing import Dict


class GoogleSheetManager:

    def __init__(self, agcm):
        self.agcm = agcm
        self.row = 1
        self.is_row_updated = False

    async def authorize(self):
        agc = await self.agcm.authorize()
        return agc

    async def update_row(self, worksheet):
        str_list = list(filter(None, await worksheet.col_values(8)))
        self.row = str(len(str_list) + 1)

    async def push_data(self, data: Dict[str, str]):
        agc = await self.authorize()
        ss = await agc.open("MAIN")
        ws = await ss.get_worksheet(0)

        if self.is_row_updated:
            print('upped once')
            self.row += 1
        else:
            self.is_row_updated = True
            await self.update_row(ws)
        print(self.row)
        cells = await ws.range('%s:%s' % (f"A{self.row}", f"M{self.row}"))

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
        print("All done!")"""