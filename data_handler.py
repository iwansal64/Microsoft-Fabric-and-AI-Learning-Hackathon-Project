import pandas as pd

class DataHandler:
    def __init__(self, data_path:str):
        self.main_data = pd.read_csv(filepath_or_buffer=data_path)