def get_data(username):
    user = User.query.filter_by(username=username).first()
    return Data.query.filter_by(user_id=user.id)