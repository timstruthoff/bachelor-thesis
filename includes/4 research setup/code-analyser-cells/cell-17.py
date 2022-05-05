pmDataAccumulated = pmData.copy()

pmDataAccumulated['storypoints'] = pmDataAccumulated['storypoints'].cumsum()
pmDataAccumulated
draw_plot(pmDataAccumulated)