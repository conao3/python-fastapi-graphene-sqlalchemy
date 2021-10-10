import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from . import schema


class Department(SQLAlchemyObjectType):
    class Meta:
        model = schema.Department
        interfaces = (graphene.relay.Node,)


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = schema.Employee
        interfaces = (graphene.relay.Node,)


class Jobhist(SQLAlchemyObjectType):
    class Meta:
        model = schema.Jobhist
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    departments = SQLAlchemyConnectionField(Department.connection)
    employees = SQLAlchemyConnectionField(Employee.connection)
    jobhists = SQLAlchemyConnectionField(Jobhist.connection)


schema = graphene.Schema(query=Query)
