measuresToExamine = {}

for measure in MEASURE_MAPPING:
    for parserMeasure in MEASURE_MAPPING[measure]:
        if resultsInfo[parserMeasure]['valid']:
            measuresToExamine[measure] = parserMeasure
            break