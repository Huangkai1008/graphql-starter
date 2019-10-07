import graphene

from graphql_starter.db.link import Link


class LinkType(graphene.ObjectType):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    async def resolve_links(self, info):
        all_links = await Link.all()
        return all_links


class CreateLinkMutation(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    class Arguments:
        url = graphene.String(required=True)
        description = graphene.String(required=True)

    async def mutate(self, info, url: str, description: str):
        link = await Link.create(url=url, description=description)
        return CreateLinkMutation(
            id=link.id, url=link.url, description=link.description
        )


class Mutation(graphene.ObjectType):
    create_link = CreateLinkMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
