from dataclasses import dataclass
import pandas as pd

from lx_notams.models.notam.re_maps import REGEX_HEADER_FEATURE_MAPS, REGEX_Q_FEATURE_MAPS

import re

MAPS = {
    'Q': REGEX_Q_FEATURE_MAPS,
    'header': REGEX_HEADER_FEATURE_MAPS
}

class NotamProcessor:
    @staticmethod
    def col_from_list(l: list):
        pd.DataFrame()

    @staticmethod
    def apply_regex_columns(df: pd.DataFrame, map: dict, col: str = 'fulltext'):
        df[col].apply()

    @staticmethod
    def _apply_regex_feature_map(field: str, map: dict):
        
        for k, v in map.items():
                
            m = re.match(v['regex'], field)
            
            if 'type' in v:
                result = v['type'](next((m[i] for i in v['indexes'] if m[i]), None))
                if k in MAPS.keys():
                    yield from NotamProcessor._apply_regex_feature_map(result, MAPS[k])
                yield {k, result}
            else:
                joint_match = ' '.join([m[i] for i in v['indexes'] if m[i]])
                if (k in MAPS.keys()) and joint_match:
                    yield from NotamProcessor._apply_regex_feature_map(joint_match, MAPS[k])
                yield {k: joint_match if joint_match else None}
    

@dataclass
class DbNotam:
    
    rvid: str
    fulltext: str
    supress: float
    notamcode: str
    
    
