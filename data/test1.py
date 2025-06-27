import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase



class Test1(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'test1'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), nullable=True)
    a1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    a2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    q = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    user = orm.relationship('User')