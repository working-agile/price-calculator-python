class DataProcessor:
    value = 0
    list = []

    @staticmethod
    def calculate_data(next):
        DataProcessor.value = 0

        for i in range(len(DataProcessor.list)):
            if next and DataProcessor.list[i].days > 0:
                DataProcessor.list[i].days -= 1

            if DataProcessor.list[i].days <= 10:
                if DataProcessor.list[i].days <= 1 or (DataProcessor.list[i].avail < 3 and DataProcessor.list[i].days <= 5):
                    DataProcessor.list[i].current = DataProcessor.list[i].full
                else:
                    if DataProcessor.list[i].type == "CSD":
                        DataProcessor.list[i].current = DataProcessor.list[i].full - (DataProcessor.list[i].days * 30)
                    else:
                        DataProcessor.list[i].current = DataProcessor.list[i].full - (DataProcessor.list[i].days * 20)
            
            elif DataProcessor.list[i].days > 10:
                if DataProcessor.list[i].days <= 1 or (DataProcessor.list[i].avail < 3 and DataProcessor.list[i].days <= 5):
                    DataProcessor.list[i].current = DataProcessor.list[i].full
                else:
                    if DataProcessor.list[i].type == "CSM":
                        DataProcessor.list[i].current = DataProcessor.list[i].full - 500
                    else:
                        DataProcessor.list[i].current = DataProcessor.list[i].full - 400

            if DataProcessor.list[i].type == "CSD" and DataProcessor.list[i].current < 900:
                DataProcessor.list[i].current = 900
            elif DataProcessor.list[i].type == "CSM" and DataProcessor.list[i].current < 1000:
                DataProcessor.list[i].current = 1000
            elif DataProcessor.list[i].type == "CSPO" and DataProcessor.list[i].current < 1200:
                DataProcessor.list[i].current = 1200

            DataProcessor.value += (DataProcessor.list[i].avail * DataProcessor.list[i].current)
