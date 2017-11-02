def data():
    if request.method == 'POST':
        check_number = data_number_check(request.form.get('data'))
        if check_number:
            enter_data(request.form.get('data'))
            return redirect('/my_data')
        else:
            return render_template('data.html', error='Please follow the format for entering data.')
    return render_template('data.html')