measureResultsNormalized = measureResults.copy()

for measure in measureResults.columns:
    firstNumber = measureResults[measure].iloc[0]
    lastNumber = measureResults[measure].iloc[-1]
    measureResultsNormalized[measure] = (measureResultsNormalized[measure] - firstNumber) / (lastNumber - firstNumber)

measureResultsNormalized
# draw_plot(measureResultsNormalized)
    