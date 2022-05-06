resultsInfo = {}

for seriesName in measures:
    series = codeAnalysisInput[seriesName]
    numberOfNaN = series.isna().sum()
    proportionOfInvalid = numberOfNaN / len(series)

    if proportionOfInvalid > 0.1:
        valid = False
    else:
        valid = True
    
    resultsInfo[seriesName] = {
        'numberOfNaN': numberOfNaN,
        'proportionOfInvalid': proportionOfInvalid,
        'valid': valid
    }