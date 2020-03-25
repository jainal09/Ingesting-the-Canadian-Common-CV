from rest_framework.response import Response
from rest_framework.views import APIView
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from rest_framework import status
client = Elasticsearch(hosts="elasticsearch")

'''
This is GET request api for the display of data according to the search result and have been implemented
by ElasticSearch which is a smart search as it uses NLP for implementation of the Analyzers to index the
content to be searched

Endpoint for searching - http:/smart_search/127.0.0.1:9200/questions/_search/?q='gene'

'''


class SmartSearch(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        data = []
        try:
            s = Search().using(
                client
            ).query(
                "multi_match",
                query=query,
                fields=['Title', 'Body', 'Tags']
            )
            response = s.execute()
            response_dict = response.to_dict()
            hits = response_dict['hits']['hits']
            for val in hits:
                data.append(val["_source"])
            data_to_send = {
                "msg" : "smart search success",
                "data" : data
            }
            return Response(data=data_to_send, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status= status.HTTP_500_INTERNAL_SERVER_ERROR)