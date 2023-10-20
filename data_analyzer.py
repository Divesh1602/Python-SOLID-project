class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_min_diff(self):
        if len(self.data) < 2:
            return None

        min_diff = float('inf')
        for i in range(1, len(self.data)):
            diff = abs(self.data[i][0] - self.data[i-1][0])
            if diff < min_diff:
                min_diff = diff
        return min_diff
