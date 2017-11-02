def my_data():
    if request.args.get('entry_id'):
        data_set = get_set(request.args.get('entry_id'))
        # the data set is in csv format and needs to be broken up into a list to use.
        data = separate_data(data_set)
        mean = get_mean(data)
        median = get_median(data)
        mode = get_mode(data)
        variance = get_variance(data)
        standard_deviation = get_standard_deviation(data)
        graph = bar_chart(data)
        return render_template('dataset.html', data=data, mean=mean, median=median, mode=mode, variance=variance,
         standard_deviation=standard_deviation, graph=graph)
    else:
        data_sets = get_data(session['username'])
        return render_template('my_data.html', data_sets=data_sets)