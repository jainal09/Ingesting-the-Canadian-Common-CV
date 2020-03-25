from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DisplayData.DisplayAllFacade import DisplayAllQuestionFacade
from DisplayData.models import QuestionModel


'''
This is GET request api for the display of the data according to the order by ViewCount or  the score but API is
not for paginated content
Endpoint for chronology - http://127.0.0.1:8000/data/?q=date
Endpoint for viewcount - http://127.0.0.1:5000/data/?q=Viewcount
Endpoint for score - http://127.0.0.1:5000/data/?q=Score
'''
class SortBy(APIView):
    def get(self,request):
        q = request.GET.get('q')
        if q == "view-count":
            orderedViewsObject = QuestionModel.objects.order_by("-ViewCount")

            allData=orderedViewsObject.values()
            dataToSend=[]
            for question in allData:
                if question["ViewCount"]==None:
                    continue
                questionid = question["Id"]
                print(questionid)
                questionData = DisplayAllQuestionFacade.getData(questionID=questionid)
                dataToSend.append(questionData)
            data_dic = {
                "msg" : "success",
                "data" : dataToSend
            }
            return Response(data=data_dic, status=status.HTTP_200_OK)

        elif q=="score":

            orderedScoreObject = QuestionModel.objects.order_by("-Score")
            allData=orderedScoreObject.values()
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