pmDataResampled = pmDataNormalized.resample('60S').mean()
pmDataInterpolated = pmDataResampled.interpolate(method='linear')
pmDataResampledToHours = pmDataInterpolated.resample('1H').mean()