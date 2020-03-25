from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DisplayData.DisplayAllFacade import DisplayAllQuestionFacade
from DisplayData.models import QuestionModel
'''
This is GET request api for the display of the data according to the order by chronology but API is
not for paginated content
Endpoint for chronology - http://127.0.0.1:8000
'''
class Default(APIView):
    def get(self, request):
        orderedViewsObject = QuestionModel.objects.order_by('-CreationDate')
        allData=orderedViewsObject.values()
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