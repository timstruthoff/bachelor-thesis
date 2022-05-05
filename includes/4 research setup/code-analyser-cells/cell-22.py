# Make sure that the first element is zero and the last is one
dataMergedNormalized = dataMerged.copy()

for column in dataMergedNormalized.columns:
    firstNumber = dataMergedNormalized[column].iloc[0]
    lastNumber = dataMergedNormalized[column].iloc[-1]
    dataMergedNormalized[column] = (dataMergedNormalized[column] - firstNumber) / (lastNumber - firstNumber)