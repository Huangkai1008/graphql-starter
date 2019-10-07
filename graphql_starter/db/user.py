from tortoise import fields

from tortoise.models import Model
from passlib.hash import pbkdf2_sha256

__all__ = ['User']


class User(Model):
    """用户模型"""

    id = fields.IntField(pk=True)
    username = fields.CharField(128)
    password_hash = fields.CharField(256)
    email = fields.CharField(128)

    def hash_password(self, password):
        """加密密码"""
        self.password_hash = pbkdf2_sha256.hash(password)

    def check_password(self, password):
        """验证密码"""
        return pbkdf2_sha256.verfiy(password, self.password_hash)
