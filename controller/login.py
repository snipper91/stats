def login():
    if request.method == 'POST':
        # check_user either returns true or a dict with an error message.
        user = check_user(request.args.get('username'),request.args.get('password'))
        if user:
            session['username'] = request.args.get('username')
            return redirect('/data')
        else:
            return render_template('/login', user)
    else:
        return render_template('/login')