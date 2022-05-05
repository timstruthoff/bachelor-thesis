plt.style.use(['science','ieee'])
plt.rcParams.update({'figure.figsize': (12, 5), 'figure.dpi': 400})

def draw_plot(data):
    
    plt.xlabel('Time')
    plt.ylabel('Values')
    
    for seriesName in data.columns:
        plt.plot(data.index, data[seriesName], linewidth=0.3, label=seriesName)

    plt.gcf().autofmt_xdate()
    plt.grid(which='minor', color='lightgrey', linewidth=0.2, axis='x')
    plt.grid(which='major', color='grey', linewidth=0.2, axis='x')
    plt.legend(loc="upper left")
    plt.show()