from main import db, User, Data

def bar_chart(data):
    frequency = []
    values = []
    for point in data:
        if point in values:
            index = values.index(point)
            frequency[index] += 1
        else:
            frequency.append(1)
            value.append(point)
    return plt.bar(values, frequency)

def check_signup(username, password, verify):

    error = {'user_error':'', 'password_error':''}

    # Check that a username was entered.
    if username == '':
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

def data_number_check(data):

    is_digit = True
    for digit in data:
        if digit.isdigit() or digit == ',':
            continue
        else:
            is_digit = False
    return is_digit

def enter_data(data):
    new_data = Data(data)
    db.session(Data)
    db.session.commit()

def get_data(username):
    user = User.query.filter_by(username=username).first()
    return Data.query.filter_by(user_id=user.id)

def get_mean(data):
    return statistics.mean(data)

def get_median(data):
    return statistics.median(data)

def get_mode(data):
    return statistics.mode(data)

def get_set(entry_id):
    return Data.query.filter_by(id=entry_id).first()

def get_standard_deviation(data):
    return statistics.stdev(data)

def get_variance(data):
    return statistics.variance(data)

def logout_user(username):
    del session['username']
    return

def separate_data(data_set):
    data_str = data_set.split(',')
    data = int(data_str)
    return data

def create_user(username, password):
    password_hash = hashlib.sha256(password).hexdigest()
    new_user = User(username, password_hash)
    db.session(new_user)
    db.session.commit()