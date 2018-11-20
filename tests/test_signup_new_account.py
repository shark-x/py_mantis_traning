
import string
import random


def random_username(prefix, maxlen):
    symbols = string.ascii_letters
    some_user = prefix + "".join([random.choice(symbols) for i in range(maxlen)])
    return some_user


def test_signup_new_account(app):
    username = random_username("user_", 10)
    password = "test"
    email = username + "@localhost"
    app.james.ensure_user_exist(username, password)
    app.signup.new_user(username, email, password)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()

