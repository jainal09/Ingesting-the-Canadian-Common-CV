import peewee
import os
from lxml import etree as ET
import datetime
import time
'''
This the file for populating the database directly from the xml file to the sqlite database in according to the
desired row and column
'''
db = peewee.SqliteDatabase('db.sqlite3')

class QuestionModel(peewee.Model):
    Id = peewee.IntegerField(primary_key=True)
    post_type_id = peewee.IntegerField()
    CreationDate = peewee.DateTimeField(null=True)
    Score = peewee.IntegerField(null=True)
    Body = peewee.TextField(null=True)
    ViewCount = peewee.IntegerField(null=True)
    OwnerUserId = peewee.CharField(null=True,max_length=20)
    LastActivityDate = peewee.DateTimeField(null=True)
    Title = peewee.TextField(null=True)
    Tags = peewee.TextField(null=True)
    AnswerCount = peewee.IntegerField(null=True)
    CommentCount = peewee.IntegerField(null=True)

    class Meta:
        database = db
        db_table = 'question_table'


class AnswerModel(peewee.Model):
    Id = peewee.IntegerField(primary_key=True, default=None)
    post_type_id = peewee.IntegerField()
    parent_id = peewee.ForeignKeyField(QuestionModel, backref='answer_table')

    CreationDate = peewee.DateTimeField(default=datetime.date.today)
    Score = peewee.IntegerField()
    Body = peewee.TextField()
    OwnerUserId = peewee.CharField(max_length=20)
    LastActivityDate = peewee.DateTimeField(default=datetime.date.today)

    CommentCount = peewee.IntegerField(default=0)

    class Meta:
        database = db
        db_table = 'answer_table'

print("Please Wait populating the Datbase ---------------->")
AnswerModel.create_table()
QuestionModel.create_table()


#here to get the relation the thing


file_name = "bioinformatics_posts_se.xml"
file_path = os.path.abspath(os.path.join(file_name))

tree = ET.parse(file_path)
#made 2 lists
questions = []
answers = []
questions_data = []
answers_data = []
#zipped them or mapped them and according to the posttype id
for elem1 , elem2 in zip(tree.xpath("./row[@PostTypeId='1']"), tree.xpath("./row[@PostTypeId='2']") ):
    questions.append(elem1.attrib["Id"])
    answers.append(elem2.attrib["ParentId"])
    questions_data.append(elem1.attrib)
    answers_data.append(elem2.attrib)



diffrence = [x for x in answers if x not in questions]
myset = set()

for elements in diffrence:
    myset.add(elements)



for ansids in myset:

    dic_to_add = {
                    'Id': ansids,
                     'PostTypeId': '1',
                    'CreationDate': None,
                    'Score': None,
                    'ViewCount': None,
                    'Body': None,
                    'OwnerUserId': None,
                    'LastEditorUserId': None,
                    'LastEditDate': None,
                    'LastActivityDate' : None,
                    'Title':None,
                    'Tags': None,
                    'AnswerCount': None,
                    'CommentCount': None
           }
    questions_data.append(dic_to_add)


for elem in questions_data:
    new_question = QuestionModel.create(Id=elem['Id'],
                            CreationDate=elem['CreationDate'],
                            Score=elem['Score'],
                            ViewCount=elem['ViewCount'],
                            Body=elem['Body'],
                            post_type_id=elem['PostTypeId'],
                            OwnerUserId=elem['OwnerUserId'],
                            LastActivityDate=elem['LastActivityDate'],
                            Title=elem['Title'],
                            Tags=elem['Tags'],
                            AnswerCount=elem['AnswerCount'],
                            CommentCount=elem['CommentCount'])
    new_question.save()




for elem in answers_data:

    new_answer = AnswerModel.create(Id=elem['Id'],
                            CreationDate=elem['CreationDate'],
                            Score=elem['Score'],
                            Body=elem['Body'],
                            post_type_id=elem['PostTypeId'],
                            OwnerUserId=elem['OwnerUserId'],
                            LastActivityDate=elem['LastActivityDate'],
                            parent_id=elem['ParentId'],
                            CommentCount=elem['CommentCount'])


    new_answer.save()
print("*************Done! Populating the Database!*************")