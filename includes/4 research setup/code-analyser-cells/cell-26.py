plt.rcParams.update({'figure.figsize': (12, 6), 'figure.dpi': 400})

figure, (ax1, ax2) = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios': [7, 1]})

figure.suptitle(PROJECT_TITLE)
figure.tight_layout()

ax1.plot(finalData.index, finalData['storypoints'], linewidth=0.7, label=LOCALIZATION_STRINGS['storypoints'], linestyle='solid', color=COLORS['storypoints'])

for measure in MEASURE_MAPPING:
    ax1.plot(finalData.index, finalData[measure], linewidth=0.3, label=LOCALIZATION_STRINGS[measure], linestyle='solid', color=COLORS[measure])

ax1.set_ylabel(LOCALIZATION_STRINGS['value'])
ax2.set_ylabel(LOCALIZATION_STRINGS['difference'])

ax1.set_xlabel(LOCALIZATION_STRINGS['time'])
ax2.set_xlabel(LOCALIZATION_STRINGS['time'])

ax2.fill_between(difference.index, difference, linewidth=0.7, label=LOCALIZATION_STRINGS['difference'], facecolor=COLORS['difference'])

limit = max([abs(difference.max()), abs(difference.min())]) + 0.1
ax2.set_ylim([-limit, limit])

ax = plt.gca()

ax.xaxis.set_major_locator(mdates.DayLocator(interval=30))
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=5))

figure.autofmt_xdate()
ax1.grid(which='minor', color='lightgrey', linewidth=0.2, axis='x')
ax1.grid(which='major', color='grey', linewidth=0.2, axis='x')
ax1.legend(loc="upper left")

figure.savefig(RESULT_PATH + '/plot.pdf')
figure.savefig(RESULT_PATH + '/plot.png')