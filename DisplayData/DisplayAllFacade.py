
from DisplayData.models import QuestionModel
'''
This class is generally used for the GET request and send the json data to the frontend 
'''

class DisplayAllQuestionFacade:
    def getData(questionID):
        createQuestionObj = QuestionModel.objects.get(Id = questionID)
        post_type_id = createQuestionObj.post_type_id
        CreationDate = createQuestionObj.CreationDate
        Score=createQuestionObj.Score
        Body = createQuestionObj.Body
        ViewCount=createQuestionObj.ViewCount
        OwnerUserId=createQuestionObj.OwnerUserId
        LastActivityDate=createQuestionObj.LastActivityDate
        Title = createQuestionObj.Title
        Tags= createQuestionObj.Tags
        AnswerCount = createQuestionObj.AnswerCount
        CommentCount = createQuestionObj.CommentCount



        finalDic = {
            "questionID" : questionID,
            "post_type_id": post_type_id,
            "CreationDate" : CreationDate,
            "Score":Score,
            "Body":Body,
            "ViewCount":ViewCount,
            "LastActivityDate":LastActivityDate,
            "Title": Title,
            "Tags": Tags,
            "AnswerCount": AnswerCount,
            "CommentCount": CommentCount,
            "OwnerUserId": OwnerUserId,


        }

        return finalDic
