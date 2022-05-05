CODE_CSV_PATH = './input/dtcnda/input-code.csv'
PM_CSV_PATH = './input/dtcnda/input-jira.csv'
PROJECT_TITLE = 'DIL NDA Projekt Verhältnis von Storypoints und Codekomplexitätsmetriken'

PM_STORYPOINT_COLUMN = 'Custom field (Story Points)'
PM_DATE_COLUMN = 'Resolved'
PM_ISSUE_COLUMN = 'Issue key'
RESULT_PATH = 'result/dtcnda'

MEASURE_MAPPING = {
    'logicalLinesOfCode': ['platoSlocLogical', 'multimetricLoc'],
    'cyclomaticComplexity': ['lizardCyclomaticComplexity', 'platoCyclomaticComplexity', 'multimetricCyclomaticComplexity'],
    'halsteadEffort': ['platoHalsteadEffort', 'multimetricHalsteadEffort'],
    'indendationComplexity': ['indentationComplexity']
}

COLORS = {
    'storypoints': '#001219',
    'logicalLinesOfCode': '#AE2012',
    'cyclomaticComplexity': '#005F73',
    'halsteadEffort': '#94D2BD',
    'indendationComplexity': '#EE9B00',
    'difference': '#CCC9C2'
}

LOCALIZATION_STRINGS = {
    'storypoints': 'Story Points',
    'logicalLinesOfCode': 'Logische Codezeilen',
    'cyclomaticComplexity': 'Zyklomatische Komplexität',
    'halsteadEffort': 'Halstead Aufwand',
    'indendationComplexity': 'Einrückungskomplexität',
    'difference': 'Unterschied',
    'value': 'Wert',
    'time': 'Zeit',
    'correlation': 'Korrelation',
    'spearman': 'Spearman Rangkorrelationskoeffizient',
    'pearson': 'Pearson Produkt-Moment-Korrelation',
    'kendall': 'Kendall Rangkorrelationskoeffizient'
}

CORRELATION_MIN = 0.5
CORRELATION_MAX = 1
