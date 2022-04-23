import hashlib
import os
from . import users, db_session
from .users import User


def hashing_password(password: str) -> tuple:
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt, key


def password_verification(password: str, name: str) -> bool:
    db_sess = db_session.create_session()
    salt = db_sess.query(User).filter(User.name == name).salt  # Получение соли
    key = db_sess.query(User).filter(User.name == name).key
    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    if key != new_key:
        return False
    else:
        return True
