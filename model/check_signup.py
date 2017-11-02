def check_signup(username, password, verify):

    error = {'user_error':'', 'password_error':''}

    # Check that a username was entered.
    if username = '':
        error['user_error'] = 'Please enter a username.'
        return error

    # Check that a password was entered.
    if password == '':
        error['password_error'] = 'Please enter a password.'
        return error

    existing_user = User.query.filter_by(username=username).first()
    # Check that the username is not already in use.
    if existing_user:
        error['user_error'] = 'That username is already in use.'
        return error

    # Check that the password was correctly entered twice.
    if password != verify:
        error['password_error'] = 'Your passwords did not match.'
        return error
