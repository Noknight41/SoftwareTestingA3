import pylightxl as xl 

class Excel:
    def __init__(self, filePath):
        self.db = xl.readxl(filePath)
        
    def readData(self, sheetName):
        table = self.db.ws(sheetName).ssd(keycols="Index", keyrows="Index")
        return table[0]['data']
    
    def writeData(self, mydata, fileName):
        db = xl.Database()

        db.add_ws(ws="Output")

        for row_id, data in enumerate(mydata, start=1):
            for col_id in range(1, len(data)+1):
                db.ws(ws="Output").update_index(row=row_id, col=col_id, val=data[col_id - 1])

        xl.writexl(db=db, fn="Output/" + fileName + ".xlsx")

