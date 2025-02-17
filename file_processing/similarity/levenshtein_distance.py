from file_processing.similarity.file_metric_strategy import FileMetricStrategy

class LevenshteinDistance(FileMetricStrategy):
    def calculate(self):
        from Levenshtein import distance

        text1 = self.file1.metadata['text']
        text2 = self.file2.metadata['text']

        lev_dist = distance(text1, text2)

        return lev_dist
