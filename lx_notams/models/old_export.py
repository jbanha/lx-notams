import pandas as pd
from pathlib import Path
from dataclasses import dataclass    

class OldExport:
    
    @staticmethod
    def from_dir(directory: Path):
        
        dfs = []

        for p in directory.glob('*'):
            print('Processing:', p)
            with p.open() as f:
                lines = f.readlines()
                
            if len(list(set([len(line.split(';')) for line in lines]))) > 1:
                print('Different number of columns in file:', p)
                continue
            
            dfs.append(pd.read_csv(p, sep=';'))
            
        self.df = pd.concat(dfs)
        