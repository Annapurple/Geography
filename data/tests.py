import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase



class Tests(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'tests'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), nullable=True)
    test1 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    test2 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    test3 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    test4 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    test5 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    test6 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    test7 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    test8 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    user = orm.relationship('User')