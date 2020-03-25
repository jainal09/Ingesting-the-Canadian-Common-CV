from django.core.management.base import BaseCommand, CommandError
from elasticsearch_dsl import Search, Index, connections
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from DisplayData.models import QuestionModel
from DisplayData.document import QuestionIndex
from elasticsearch_dsl import connections
import os
import time

print("I am alive!!")
ES_HOST = os.environ.get('ES_HOST')
ES_PORT = os.environ.get('ES_PORT')
'''
This is the most important file for the elasticsearch as it is the indexer file for the indexes of the
question model which indexes it to the middleware server of the elasticseaerch 

'''
connections.create_connection(
            hosts=[{'host': ES_HOST, 'port': ES_PORT}])
class Command(BaseCommand):

    def handle(self, *args, **options):
        print(ES_HOST)
        print(ES_PORT)
        es = Elasticsearch(
            [{'host': ES_HOST, 'port': ES_PORT}],
            index="question1"
        )
        question_index = Index('question1')
        question_index.document(QuestionIndex)
        result = bulk(
            client=es,
            actions=(que.indexing() for que in QuestionModel.objects.all())
        )

        print('Indexed questions.')

        print(result)