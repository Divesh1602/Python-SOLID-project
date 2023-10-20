class DataExtractor:
    def __init__(self, file_name, column1, column2):
        self.file_name = file_name
        self.column1 = column1
        self.column2 = column2

    def extract_data(self):
        data = []
        with open(self.file_name, 'r') as file:
            next(file)
            for line in file:
                columns = line.strip().split(',')
                if len(columns) >= max(self.column1, self.column2):
                    data.append((float(columns[self.column1]), float(columns[self.column2])))
        return data
