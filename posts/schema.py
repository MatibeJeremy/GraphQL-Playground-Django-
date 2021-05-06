import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType

from .models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()


# Mutation class
class CreatePost(graphene.Mutation):
    # output of the mutation
    id = graphene.Int()
    title = graphene.String()
    by = graphene.Field(UserType)

    # Defines data you can send to the server
    class Arguments:
        title = graphene.String()

    # Creates a post in the database using the data sent by the user
    def mutate(self, info, title):
        user = info.context.user or None
        post = Post(title=title, by=user)
        post.save()

        return CreatePost(
            id=post.id,
            title=post.title,
            by=post.by,
        )


# creates a mutation class with a field to be resolved
class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
