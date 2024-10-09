from typing import Dict


class GoogleSheetManager:

    def __init__(self, gc):
        self.ws = gc.open("Ответы MixQuiz").sheet1
        self.row = self.update_row()

    def update_row(self) -> int:
        str_list = list(filter(None, self.ws.col_values(1)))
        return len(str_list)

    def push_data(self, data: Dict[str, str]):
        self.row += 1
        cells = self.ws.range('%s:%s' % (f"A{self.row}", f"M{self.row}"))

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

        self.ws.update_cells(cells)
        print("All done!")