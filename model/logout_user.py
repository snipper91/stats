def logout_user(username):
    del session['username']
    return