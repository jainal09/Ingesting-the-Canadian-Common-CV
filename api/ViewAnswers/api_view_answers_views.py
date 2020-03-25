from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DisplayData.models import QuestionModel, AnswerModel

class AnswersId(APIView):
    def get(self, request):
        try:
            search_query = request.query_params.get('id')
            qobj_id = QuestionModel.objects.get(Id=search_query)
            aobj = AnswerModel.objects.filter(parent_id =qobj_id)
            answer_list = []
            for vals_id in aobj.values():
                answer_list.append(vals_id)
            if len(answer_list) is 0:
                data_dic = {
                    "msg": "success",
                    "data": "No answers found"
                }
            else:
                data_dic = {
                    "msg": "success",
                    "data": answer_list
                }
            return Response(data=data_dic, status=status.HTTP_200_OK)
        except QuestionModel.DoesNotExist:
            data_dic = {
                "msg": "success",
                "data": "No such questions found"
            }
            return Response(data=data_dic, status=status.HTTP_200_OK)
class AnswersTitle(APIView):
    def get(self, request):
        search_query = request.query_params.get('title')
        try:
            qobj_title = QuestionModel.objects.get(Title=search_query)
            aobj = AnswerModel.objects.filter(parent_id=qobj_title)
            answer_list = []
            for vals_title in aobj.values():
                answer_list.append(vals_title)
            if len(answer_list) is 0:
                data_dic = {
                    "msg": "success",
                    "data": "No answers found"
                }
            else:
                data_dic = {
                    "msg": "success",
                    "data": answer_list
                }
            return Response(data=data_dic, status=status.HTTP_200_OK)
        except QuestionModel.DoesNotExist:
            data_dic = {
                "msg": "success",
                "data": "No such questions found"
            }
            return Response(data=data_dic, status=status.HTTP_200_OK)

