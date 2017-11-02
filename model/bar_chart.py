def bar_chart(data):
    frequency = []
    values = []
    for point in data:
        if point in values:
            index = values.index(point)
            frequency[index] += 1
        else:
            frequency.append(1)
            value.append(point)
    return plt.bar(values, frequency)