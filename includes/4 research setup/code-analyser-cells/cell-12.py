measureResultsResampled = measureResultsNormalized.resample('60S').mean()
measureResultsInterpolated = measureResultsResampled.interpolate(method='linear')
measureResultsResampledToHours = measureResultsInterpolated.resample('1H').mean()