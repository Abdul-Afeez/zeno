import csv


class ZenoCSVParser:
    min_length = 0

    def __init__(self, file_location):
        self.file_location = file_location

    def validate_extension(self, ext):
        return self.file_location.lower().endswith(ext)

    def receive_sense_training(self, header=('id', 'timestamp', 'temperature', 'duration')):
        self.min_length = len(header)

    def parse(self):
        with open(self.file_location, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                yield row

        return []
