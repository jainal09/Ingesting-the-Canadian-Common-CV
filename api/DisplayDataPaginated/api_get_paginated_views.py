from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DisplayData.DisplayAllFacade import DisplayAllQuestionFacade
from DisplayData.models import QuestionModel
from django.core.paginator import Paginator
'''
This is GET request api for the display of the data according to the order by ViewCount or  the score but API is
for paginated content which is 10 questions for a page

Endpoint for viewcount - http://127.0.0.1:8000/pages/<page-no.>/?q=ViewCount
Endpoint for viewcount - http://127.0.0.1:8000/pages/<page-no>/?q=Score

'''
orderedViewsObject = QuestionModel.objects.order_by('-ViewCount')
p = Paginator(orderedViewsObject, 10)
class SortBy(APIView):
    def get(self,request, page):

        query = request.query_params.get('q')
        if query == "ViewCount":

            page_object = p.get_page(page)
            p_object_list = page_object.object_list
            allData=p_object_list.values()
            dataToSend=[]
            for question in allData:
                if question["ViewCount"]==None:
                    continue
                questionid = question["Id"]
                questionData = DisplayAllQuestionFacade.getData(questionID=questionid)
                dataToSend.append(questionData)
            data_dic = {
                "msg" : "success",
                "data" : dataToSend
            }
            return Response(data=data_dic, status=status.HTTP_200_OK)

        elif query=="Score":

            orderedScoreObject = QuestionModel.objects.order_by("Score")
            p = Paginator(orderedScoreObject, 10)
            page_object = p.get_page(page)
            p_object_list = page_object.object_list
            allData=p_object_list.values()
            dataToSend = []
            for question in allData:
                if question["Score"]==None:
                    continue
                questionid=question["Id"]

                questionData=DisplayAllQuestionFacade.getData(questionID=questionid)
                dataToSend.append(questionData)
            data_dic = {
                "msg": "success",
                "data": dataToSend
            }

            return Response(data=data_dic, status=status.HTTP_200_OK)
        else:
            return  Response(status=status.HTTP_400_BAD_REQUEST)
class Count(APIView):
    def post(self, request):
        count = p.count
        return Response(data=count, status= status.HTTP_200_OK)