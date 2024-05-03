from pathlib import Path
import pandas as pd

class DatasetImporter:
    @staticmethod
    def list_file(path: Path):
        with open(path, 'r') as f:
            return f.readlines()
        
    @staticmethod
    def df_file(path: Path):
        return pd.read_csv(path)