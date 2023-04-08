import base64
import hashlib
import hmac
from flask import current_app

def __generate_password_digest(password):
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password):
    return base64.b64encode(__generate_password_digest(password))

def compare_password(password_hash, password):
    return hmac.compare_digest(
        base64.b64decode(password_hash),
        hashlib.pbkdf2_hmac("sha256",
                            password.encode('utf-8'),
                            salt=current_app.config["PWD_HASH_SALT"],
                            iterations=current_app.config["PWD_HASH_ITERATIONS"]
                            )
    )