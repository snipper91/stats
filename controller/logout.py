def logout():
    logout_user(request.session.get(username))
    return redirect('/login')