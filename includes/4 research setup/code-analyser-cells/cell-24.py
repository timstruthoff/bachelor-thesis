# Calculate the mean of all values
mean = finalData[['logicalLinesOfCode', 'cyclomaticComplexity', 'halsteadEffort', 'indendationComplexity']].mean(axis=1)

finalDataDescribed = finalData.copy()
finalDataDescribed['mean'] = mean

finalDataDescribed