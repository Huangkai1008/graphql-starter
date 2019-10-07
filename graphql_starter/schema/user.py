import graphene
import passlib

from graphql_starter.db.user import User


class UserType(graphene.ObjectType):
    id = graphene.Int()
    username = graphene.String()
    password = graphene.String()
    email = graphene.String()


class CreateUserMutation(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    async def mutate(self, info, username: str, password: str, email: str):
        user = User(username=username, email=email)
        user.hash_password(password)
        user = await user.save()
        return CreateUserMutation(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
