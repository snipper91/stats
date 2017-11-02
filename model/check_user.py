def check_user(username, password):
    user = User.query.filter_by(username=username).first()
    error = {'password_error':'', 'username_error':''}
    if user:
        password_hash = hashlib.sha256(password).hexdigest()
        if user.password_hash == password_hash:
            return True
        else:
            error['password_error'] = 'Incorrect password.'
    else:
        error['username_error'] = 'Incorrect username.'
    return error