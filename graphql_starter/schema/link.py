import graphene

from graphql_starter.db.link import Link


class LinkType(graphene.ObjectType):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info):
        return Link.all()


schema = graphene.Schema(query=Query)
