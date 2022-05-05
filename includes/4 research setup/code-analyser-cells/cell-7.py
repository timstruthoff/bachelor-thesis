measures = []
for seriesName in codeAnalysisInput.columns:
    if seriesName != 'commit' and seriesName != 'timestamp':
        measures.append(seriesName)

measures