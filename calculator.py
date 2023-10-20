from data_extractor import DataExtractor
from data_analyzer import DataAnalyzer

class Calculator:
    def __init__(self, file_name, column1, column2):
        self.data_extractor = DataExtractor(file_name, column1, column2)
        data = self.data_extractor.extract_data()
        self.data_analyzer = DataAnalyzer(data)

    def execute(self):
        min_diff = self.data_analyzer.calculate_min_diff()
        return min_diff
