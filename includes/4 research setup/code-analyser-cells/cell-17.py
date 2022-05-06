pmDataAccumulated = pmData.copy()
pmDataAccumulated['storypoints'] = pmDataAccumulated['storypoints'].cumsum()