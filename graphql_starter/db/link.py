from tortoise import fields
from tortoise.models import Model

__all__ = ['Link']


class Link(Model):
    id = fields.IntField(pk=True)
    url = fields.CharField(128)
    description = fields.TextField(null=True)
