pmDataNormalized = pmDataAccumulated.copy()
lastValue = pmDataNormalized['storypoints'].iloc[-1]

pmDataNormalized['storypoints'] = pmDataNormalized['storypoints'] / lastValue
pmDataNormalized