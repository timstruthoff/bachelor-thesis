dataFrameContents = {}
for measure in measuresToExamine:
    dataFrameContents[measure] = codeAnalysisInput[measuresToExamine[measure]]

measureResults = pd.DataFrame(data=dataFrameContents)
measureResults.fillna(0, inplace=True)
measureResults