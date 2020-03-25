from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DisplayData.DisplayAllFacade import DisplayAllQuestionFacade
from DisplayData.models import QuestionModel
from django.core.paginator import Paginator
'''
This is GET request api for the display of the data according to the order by ViewCount or  the score but API is
for paginated content which is 10 questions for a page

Endpoint for viewcount - http://127.0.0.1:8000/pages/<page-no.>/?q=view-count
Endpoint for viewcount - http://127.0.0.1:8000/pages/<page-no>/?q=score

'''

class SortBy(APIView):
    def get(self,request, page):

        query = request.query_params.get('q')
        if query == "view-count":
            orderedScoreObject = QuestionModel.objects.order_by("-ViewCount")
            paginator_object = Paginator(orderedScoreObject, 10)
            page_count = paginator_object.count
            if page > page_count:
                data_to_send = "Page not found : max pages are " + str(page_count)
                return Response(data=data_to_send, status=status.HTTP_400_BAD_REQUEST)
            else:
                page_object = paginator_object.get_page(page)
                p_object_list = page_object.object_list
                allData = p_object_list.values()
                print(allData)
                dataToSend = []
                for question in allData:
                    questionid = question["Id"]
                    questionData = DisplayAllQuestionFacade.getData(questionID=questionid)
                    dataToSend.append(questionData)
                data_dic = {
                    "page": page,
                    "total_pages": page_count,
                    "page_data": dataToSend
                }

                data_dic = {
                    "msg": "success",
                    "data": data_dic
                }

                return Response(data=data_dic, status=status.HTTP_200_OK)

        elif query=="score":
            orderedScoreObject = QuestionModel.objects.order_by("-Score")
            paginator_object = Paginator(orderedScoreObject, 10)
            page_count = paginator_object.count
            if page>page_count:
                data_to_send = "Page not found : max pages are " + str(page_count)
                return Response(data = data_to_send, status=status.HTTP_400_BAD_REQUEST)
            else:
                page_object = paginator_object.get_page(page)
                p_object_list = page_object.object_list
                allData = p_object_list.values()
                print(allData)
                dataToSend = []
                for question in allData:
                    questionid = question["Id"]
                    questionData = DisplayAllQuestionFacade.getData(questionID=questionid)
                    dataToSend.append(questionData)
                data_dic = {
                    "page": page,
                    "total_pages": page_count,
                    "page_data": dataToSend
                }

                data_dic = {
                    "msg": "success",
                    "data": data_dic
                }

                return Response(data=data_dic, status=status.HTTP_200_OK)
class Count(APIView):
    def post(self, request):
        count = p.count
        return Response(data=count, status= status.HTTP_200_OK)