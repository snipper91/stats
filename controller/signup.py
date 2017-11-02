def signup():
    if request.method == 'POST':
        #check_signup either returns true or a dict with an error message.
        user = check_signup(request.form.get('username'), request.form.get('password'), request.form.get('verify'))
        if user:
            create_user(request.form.get('username'), request.form.get('password'))
            session['username'] = request.form.get('username')
            return redirect('/newdata')
        else:
            return render_template('signup.html', user=user)
    else:
        return render_template('signup.html')