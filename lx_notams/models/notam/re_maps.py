from pathlib import Path
from lx_notams.models.notam.processors.common import DatasetImporter

datasets_path = Path(__file__).parent.parent.parent / 'datasets'

REGEX_FEATURE_MAPS = {
    'header': {
        'regex': "(^[A-Z][0-9]{4}[/][0-9]{2} NOTAM[RN]( [A-Z][0-9]{4}[/][0-9]{2})?)\\s+Q[)].*",
        'indexes': [1]
    },
    'Q': {
        'regex': "^[A-Z][0-9]{4}[/][0-9]{2} NOTAM[RN]( [A-Z][0-9]{4}[/][0-9]{2})? Q[)]([A-Z0-9/]+) A[)].*",
        'indexes': [2]
    },
    'A': {
        'regex': "^[A-Z][0-9]{4}[/][0-9]{2} NOTAM[RN]( [A-Z][0-9]{4}[/][0-9]{2})? Q[)][A-Z0-9/]+ A[)]([A-Z]{4}( [A-Z]{4})*)\\s+B[)].*",
        'indexes': [2]
    },
    'B': {
        'regex': "^[A-Z][0-9]{4}[/][0-9]{2} NOTAM[RN]( [A-Z][0-9]{4}[/][0-9]{2})? Q[)][A-Z0-9/]+ A[)][A-Z]{4}( [A-Z]{4})*\\s+B[)]([0-9A-Z]+) .*",
        'indexes': [3]
    },
    'C': {
        'regex': "^[A-Z][0-9]{4}[/][0-9]{2} NOTAM[RN]( [A-Z][0-9]{4}[/][0-9]{2})? Q[)][A-Z0-9/]+ A[)][A-Z]{4}( [A-Z]{4})*\\s+B[)][0-9A-Z]+ C[)]([0-9A-Z]+) .*",
        'indexes': [3]
    },
    'D': {
        'regex': "^[A-Z][0-9]{4}[/][0-9]{2} NOTAM[RN]( [A-Z][0-9]{4}[/][0-9]{2})? Q[)][A-Z0-9/]+ A[)][A-Z]{4}( [A-Z]{4})* +B[)][0-9A-Z]+ C[)][0-9A-Z]+ +(D[)](\\S+.*?) +)?E[)].*",
        'indexes': [4]
    },
    'E': {
        'regex': "^[A-Z][0-9]{4}[/][0-9]{2} NOTAM[RN]( [A-Z][0-9]{4}[/][0-9]{2})? Q[)][A-Z0-9/]+ A[)][A-Z]{4}( [A-Z]{4})* +B[)][0-9A-Z]+ C[)][0-9A-Z]+ +(D[)]\\S+.*? +)?E[)](.*)\\s+F[)]\\S+.*$|^[A-Z][0-9]{4}[/][0-9]{2} NOTAM[RN]( [A-Z][0-9]{4}[/][0-9]{2})? Q[)][A-Z0-9/]+ A[)][A-Z]{4}( [A-Z]{4})* +B[)][0-9A-Z]+ C[)][0-9A-Z]+ +(D[)]\\S+.*? +)?E[)](?!.*\\s+F[)]\\S+.*)(.*)$",
        'indexes': [4, 8]
    },
    'F': {
        'regex': "^.*\\sE[)](?!.*\\s+F[)]\\S+.*)(.*)$|^.*\\s+F[)](.*)\\s+G[)]\\S+.*$|^.*\\sF[)](?!.*\\s+G[)]\\S+.*)(.*)$",
        'indexes': [2, 3]
    },
    'G': {
        'regex': "^.*\\sE[)](?!.*\\s+G[)]\\S+.*)(.*)$|^.*\\s+G[)](.*)$",
        'indexes': [2]
    }
}

REGEX_Q_FEATURE_MAPS = {
    'lat_deg': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}[A-Z]{2}/[A-Z]+/[A-Z]+/[A-Z]+/[0-9]+/[0-9]+/([0-9]{2})[0-9]{2}[A-Z].*",
        'indexes': [1],
        'type': float
    },
    'lat_min': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}[A-Z]{2}/[A-Z]+/[A-Z]+/[A-Z]+/[0-9]+/[0-9]+/[0-9]{2}([0-9]{2})[A-Z].*",
        'indexes': [1] ,
        'type': float   
    },
    'lat_hem': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}[A-Z]{2}/[A-Z]+/[A-Z]+/[A-Z]+/[0-9]+/[0-9]+/[0-9]{2}[0-9]{2}([A-Z]).*",
        'indexes': [1]
    },
    'lon_deg': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}[A-Z]{2}/[A-Z]+/[A-Z]+/[A-Z]+/[0-9]+/[0-9]+/[0-9]{2}[0-9]{2}[A-Z]([0-9]{3})[0-9]{2}[A-Z].*",
        'indexes': [1],
        'type': float
    },
    'lon_min': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}[A-Z]{2}/[A-Z]+/[A-Z]+/[A-Z]+/[0-9]+/[0-9]+/[0-9]{2}[0-9]{2}[A-Z][0-9]{3}([0-9]{2})[A-Z].*",
        'indexes': [1],
        'type': float
    },
    'lon_hem': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}[A-Z]{2}/[A-Z]+/[A-Z]+/[A-Z]+/[0-9]+/[0-9]+/[0-9]{2}[0-9]{2}[A-Z][0-9]{3}[0-9]{2}([A-Z]).*",
        'indexes': [1]
    },
    'fir': {
        'regex': "^([A-Z]{4}).*",
        'indexes': [1]
    },
    'subject': {
        'regex': "^[A-Z]{4}/[A-Z]([A-Z]{2}).*",
        'indexes': [1]
    },
    'condition': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}([A-Z]{2}).*",
        'indexes': [1]
    },
    'traffic': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}[A-Z]{2}/([A-Z]+).*",
        'indexes': [1]
    },
    'purp': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}[A-Z]{2}/[A-Z]+/([A-Z]+).*",
        'indexes': [1]
    },
    'scope': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}[A-Z]{2}/[A-Z]+/[A-Z]+/([A-Z]+).*",
        'indexes': [1]
    },
    'flmin': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}[A-Z]{2}/[A-Z]+/[A-Z]+/[A-Z]+/([0-9]+).*",
        'indexes': [1],
        'type': int
    },
    'flmax': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}[A-Z]{2}/[A-Z]+/[A-Z]+/[A-Z]+/[0-9]+/([0-9]+).*",
        'indexes': [1],
        'type': int
    },
    'rad': {
        'regex': "^[A-Z]{4}/[A-Z][A-Z]{2}[A-Z]{2}/[A-Z]+/[A-Z]+/[A-Z]+/[0-9]+/[0-9]+/[0-9]{2}[0-9]{2}[A-Z][0-9]{3}[0-9]{2}[A-Z]([0-9]{3}).*",
        'indexes': [1],
        'type': float
    }
}

REGEX_HEADER_FEATURE_MAPS = {
    'nat': {
        'regex': ".*NOTAM([A-Z]).*",
        'indexes': [1]
    }
}

DATASET_MAP = {
    'subjects': {
        'path': datasets_path / 'subj_dataset_curated.csv',
        'import_fn': DatasetImporter.df_file,
        'rename_map': {}
    },
    'conditions': {
        'path': datasets_path / 'cond_dataset_curated.csv',
        'import_fn': DatasetImporter.df_file,
        'rename_map': {}
    },
    'contractions': {
        'path': datasets_path / 'contraction_dataset.csv',
        'import_fn': DatasetImporter.df_file,
        'rename_map': {}
    },
    'stopwords': {
        'path': datasets_path / 'english_stopwords_dataset.csv',
        'import_fn': DatasetImporter.list_file,
    },
    'ngram_exclusion': {
        'path': datasets_path / 'ngram_exclusion.csv',
        'import_fn': DatasetImporter.list_file
    },
    'special_numbers': {
        'path': datasets_path / 'special_number_dataset.csv',
        'import_fn': DatasetImporter.df_file,
        'rename_map': {}
    },
    '4lc_destinations': {
        'path': datasets_path /  '4lc_dest.csv',
        'import_fn': DatasetImporter.list_file
    },
    '4lc_alternates': {
        'path': datasets_path / '4lc_alternates.csv',
        'import_fn': DatasetImporter.list_file
    },
    '4lc_2nd_alternates_com': {
        'path': datasets_path / '4lc_2nd_alternates_com.csv',
        'import_fn': DatasetImporter.list_file
    },
    '4lc_2nd_alternates_fw': {
        'path': datasets_path / '4lc_2nd_alternates_fw.csv',
        'import_fn': DatasetImporter.list_file
        },
    '4lc_3rd_alternates_com': {
        'path': datasets_path / '4lc_3rd_alternates_com.csv',
        'import_fn': DatasetImporter.list_file
    },
    '4lc_3rd_alternates_fw': {
        'path': datasets_path / '4lc_3rd_alternates_fw.csv',
        'import_fn': DatasetImporter.list_file
    },
    '4lc_4th_alternates_com': {
        'path': datasets_path /  '4lc_4th_alternates_com.csv',
        'import_fn': DatasetImporter.list_file
    },
    '4lc_4th_alternates_fw': {
        'path': datasets_path /  '4lc_4th_alternates_fw.csv',
        'import_fn': DatasetImporter.list_file
    },
    '4lc_5th_alternates_com': {
        'path': datasets_path /  '4lc_5th_alternates_com.csv',
        'import_fn': DatasetImporter.list_file
    },
    '4lc_5th_alternates_fw': {
        'path': datasets_path /  '4lc_5th_alternates_fw.csv',
        'import_fn': DatasetImporter.list_file
    },
    '4lc_6th_alternates_com': {
        'path': datasets_path /  '4lc_6th_alternates_com.csv',
        'import_fn': DatasetImporter.list_file
    },
    '4lc_6th_alternates_fw': {
        'path': datasets_path /  '4lc_6th_alternates_fw.csv',
        'import_fn': DatasetImporter.list_file
    },
    '4lc_7th_alternates_com': {
        'path': datasets_path /  '4lc_7th_alternates_com.csv',
        'import_fn': DatasetImporter.list_file
    },
    '4lc_7th_alternates_fw': {
        'path': datasets_path /  '4lc_7th_alternates_fw.csv',
        'import_fn': DatasetImporter.list_file
    },
    'feature_names': {
        'path': datasets_path /  'feature_names.csv',
        'import_fn': DatasetImporter.list_file
    },
    'key_ngrams': {
        'path': datasets_path / 'key_ngrams.csv',
        'import_fn': DatasetImporter.df_file,
        'rename_map': {}
    }
}