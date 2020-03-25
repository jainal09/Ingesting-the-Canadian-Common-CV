from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DisplayData.models import QuestionModel
'''
This is GET request api for the display of data according to the search result and have been implemented
by basic query searching

Endpoint for searching - http://127.0.0.1:8000/search/?q='gene'

'''

class Search(APIView):
    def get(self, request):
        search_query = request.query_params.get('q')
        qobj_title = QuestionModel.objects.filter(Title__contains=search_query)
        qobj_body = QuestionModel.objects.filter(Body__contains=search_query)
        question_list_title = []
        question_list_body = []
        for vals_body in qobj_body.values():
            question_list_body.append(vals_body)
        for vals_title in qobj_title.values():
            question_list_title.append(vals_title)
        if len(question_list_title) is 0 and len(question_list_body) is 0:
            data_dic = {
                "msg": "success",
                "data": "no results found"
            }
            return Response(data=data_dic, status=status.HTTP_200_OK)
        elif len(question_list_title) is 0:
            data_to_send = {
                "title_results": "no result",
                "body_results": question_list_body
            }
            data_dic = {
                "msg": "success",
                "data": data_to_send
            }
            return Response(data=data_dic, status=status.HTTP_200_OK)
        elif len(question_list_body) is 0:
            data_to_send = {
                "title_results": question_list_title,
                "body_results": "no result"
            }
            data_dic = {
                "msg": "success",
                "data": data_to_send
            }
            return Response(data=data_dic, status=status.HTTP_200_OK)

        else:
            data_to_send = {
                "title_results": question_list_title,
                "body_results": question_list_body
            }
            data_dic = {
                "msg": "success",
                "data": data_to_send
            }
            return Response(data=data_dic, status=status.HTTP_200_OK)

