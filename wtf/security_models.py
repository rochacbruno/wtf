# coding: utf-8
from .db import db
from flask_security import UserMixin, RoleMixin
from flask_security.utils import encrypt_password


class Role(db.Document, RoleMixin):

    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

    @classmethod
    def createrole(cls, name, description=None):
        return cls.objects.create(
            name=name,
            description=description
        )


class User(db.Document, UserMixin):
    name = db.StringField(max_length=255)
    email = db.EmailField(max_length=255, unique=True)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(
        db.ReferenceField(Role, reverse_delete_rule=db.DENY), default=[]
    )
    last_login_at = db.DateTimeField()
    current_login_at = db.DateTimeField()
    last_login_ip = db.StringField(max_length=255)
    current_login_ip = db.StringField(max_length=255)
    login_count = db.IntField()
    username = db.StringField(max_length=50, required=False, unique=True)
    remember_token = db.StringField(max_length=255)
    authentication_token = db.StringField(max_length=255)

    @classmethod
    def createuser(cls, name, email, password,
                   active=True, roles=None, username=None,
                   *args, **kwargs):
        return cls.objects.create(
            name=name,
            email=email,
            password=encrypt_password(password),
            active=active,
            roles=roles,
            username=username,
            *args,
            **kwargs
        )
