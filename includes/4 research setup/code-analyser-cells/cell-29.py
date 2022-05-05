correlationPearson = finalData.corr(method='pearson')['storypoints']
correlationPearson = correlationPearson.drop('storypoints', axis=0)
correlationPearson = correlationPearson.rename('pearson')

correlationKendall = finalData.corr(method='kendall')['storypoints']
correlationKendall = correlationKendall.drop('storypoints', axis=0)
correlationKendall = correlationKendall.rename('kendall')

correlationSpearman = finalData.corr(method='spearman')['storypoints']
correlationSpearman = correlationSpearman.drop('storypoints', axis=0)
correlationSpearman = correlationSpearman.rename('spearman')

correlation = pd.DataFrame([correlationPearson, correlationKendall, correlationSpearman]).transpose()
correlation.index.names = ['Measure']

correlation.to_csv(RESULT_PATH + '/correlations.csv')
correlation