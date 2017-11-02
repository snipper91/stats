def create_user(username, password):
    password_hash = hashlib.sha256(password).hexdigest()
    new_user = User(username, password_hash)
    db.session.add(new_user)
    db.session.commit()