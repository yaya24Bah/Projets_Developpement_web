from appli.models import User
from . import db

def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username and email fields are defined correctly
    """
    assert new_user.username == 'utilisateur1'
    assert new_user.email == 'mail1@gmail.com'
    assert new_user.password == "12345678"


def test_new_user_2(client):
    response = client.get("/users/1")
    assert b"foobar" in response.data
