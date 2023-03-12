import hashlib


def validate_password(stored_password, user_supplied_password):
	return stored_password == hashlib.sha256(user_supplied_password.encode()).hexdigest()
