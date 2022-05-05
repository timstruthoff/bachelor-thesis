measureResultsResampled = measureResultsNormalized.resample('60S').mean()


measureResultsInterpolated = measureResultsResampled.interpolate(method='linear')
# measureResultsInterpolated

measureResultsResampledToHours = measureResultsInterpolated.resample('1H').mean()
# dfResampledToDays.head(10000000)

# draw_plot(measureResultsResampledToHours)

measureResultsResampledToHours