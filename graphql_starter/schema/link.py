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


schema = graphene.Schema(query=Query)
