codeAnalysisInput = codeAnalysisInput.set_index(pd.DatetimeIndex(codeAnalysisInput['timestamp']))
codeAnalysisInput.drop('timestamp', axis=1)
codeAnalysisInput = codeAnalysisInput.tz_convert('UTC')
codeAnalysisInput = codeAnalysisInput[~codeAnalysisInput['lizardCyclomaticComplexity'].isna()]
codeAnalysisInput.info()