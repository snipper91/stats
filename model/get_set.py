def get_set(entry_id):
    return Data.query.filter_by(id=entry_id).first()