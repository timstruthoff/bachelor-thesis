dataMerged = pd.merge(pmDataResampledToHours, measureResultsResampledToHours, how='inner', left_index=True, right_index=True)
dataMerged
draw_plot(dataMerged)
