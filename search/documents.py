from django_elasticsearch_dsl import DocType, Index
from blog.models import Post

posts = Index('posts')