import numpy as np
from matplotlib.colors import LinearSegmentedColormap

colors = ["#94D2BD", "#0A9396", "#005F73", "#001219"]
cmap1 = LinearSegmentedColormap.from_list("mycmap", colors)

measuresDisplay = []
correlationMeasuresDisplay = []

for measure in correlation.index.to_list():
    measuresDisplay.append(LOCALIZATION_STRINGS[measure])

for correlationMeasure in correlation.columns.to_list():
    correlationMeasuresDisplay.append(LOCALIZATION_STRINGS[correlationMeasure])

correlationNames = correlation.to_numpy()

fig, ax = plt.subplots()

im, cbar = heatmap(correlationNames, measuresDisplay, correlationMeasuresDisplay, ax=ax,
                   cmap="YlGn", cbarlabel=LOCALIZATION_STRINGS['correlation'])
texts = annotate_heatmap(im, valfmt="{x:.3f}")

fig.tight_layout()
plt.show()
fig.savefig(RESULT_PATH + '/correlation-plot.pdf')
fig.savefig(RESULT_PATH + '/correlation-plot.png')