
# Ingesting-the-Canadian-Common-CV
## Description
In this project I implemented all the requirements of the problem statement:
### Selection tests

As with the project itself, it is recommended to use Flask or Django.
>Project purely written in python django

1- First step is to ingest this file in a sqlite database. ✅
> Check ` populate.py`

2- Write an endpoint to return these posts, by default it should be in chronological order. By way of a query string in the URL, these posts may also be ordered by view count or score. ✅
>Check [Api Docs Below](#api-docs)

3- Write an endpoint to search these posts. Again, by way of a query string, filter the posts based on the presence of the search term, either in the title or body of the post.  ✅

>Check [Api Docs Below](#api-docs)

***Further I took it one step further and added the following fuctionalities on the top of these functionalities!***

 - **Elastic Search** - Using the traditional `ORM` is good but how about a very smart search with advanced smart search suggestions as you type and many more functionalities such as `tokenizing database data` , `super fast query query results` , `shards and dedicated query servers` and much more.. check more over here https://www.elastic.co/elasticsearch/features
 - **Paginated Data fetch endpoint** - The endpoint which returns  posts in chronological order and also based on view count and score queries the whole db and sends the huge response. This is dangerous and costly, hence I also created a new endpoint to fetch the same results in a `paginated approach` i.e by page by page. Each page contains only 10 results(can be calibrated and changed) making it a better cost effective, fast and efficient approach. Also the response also contains number of pages `page count` which are paginated.
 - **Show all answers of a question** : I also had created a Display answers api that displays all the answers of a question. Answers can be fetched based on `question-id` or `question-title` 

 
## Installation
```git
git clone https://github.com/jainal09/Ingesting-the-Canadian-Common-CV.git
```

**I recommend the Docker running Method as it is simple!**

## Running the Project Docker Method
*Running the Project is as simple as this!*
*As I had published a docker image specially built for this project on docker hub - https://hub.docker.com/r/jainal09/ingesting_common_cv*
```
 cd Ingesting-the-Canadian-Common-CV
 docker-compose up
```
<br />

**Or The Other Mannual approach:-**

## Running the Project Mannual Method
**Set up Virtual Environment**
```
cd Ingesting-the-Canadian-Common-CV
```
```
sudo apt install python3-pip 
```
```
pip3 install --upgrade virtualenv
```
```
sudo apt install virtualenv
```
```
virtualenv -p python3 venv 
```
```
source venv/bin/activate
```
**Install Requirements**

```
pip install -r requirements.txt
```

**Populating DB from xml**

```
python populate.py
```

**Set up elastic Search**
```
sudo apt update
sudo apt install apt-transport-https
sudo apt install openjdk-8-jdk
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
sudo sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'
sudo apt-get update && sudo apt-get install elasticsearch
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service
```
**Check if elastic search is running**
```curl
curl -X GET "localhost:9200/"
```
You should see something similar to this:

```output
{
  "name" : "kwEpA2Q",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "B-5B34LXQFqDeIYwSgD3ww",
  "version" : {
    "number" : "7.0.0",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "b7e28a7",
    "build_date" : "2019-04-05T22:55:32.697037Z",
    "build_snapshot" : false,
    "lucene_version" : "8.0.0",
    "minimum_wire_compatibility_version" : "6.7.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}

```

It will take 5-10 seconds for the service to start. If you see  `curl: (7) Failed to connect to localhost port 9200: Connection refused`, wait for a few seconds and try again.
**Setting Environment Variables**
```shell
export ES_HOST="localhost"
export ES_PORT="9200"
```
**Build Elastic Search Indexers**
```shell
python manage.py index_questions
```

**Starting Django**
```
python manage.py migrate
```
```
python manage.py runserver
```


# Api Docs

## Display Data Endpoints

 1. Endpoint to return posts in `chronological order`
GET http://127.0.0.1:8000/default/
2. Endpoint to return posts in `order by viewcount`
GET http://127.0.0.1:8000/data/?q=view-count
3.  Endpoint to return posts in `order by score`
GET http://127.0.0.1:8000/data/?q=score
4. Endpoint to return posts in **paginated** `order by viewcount`
GET http://127.0.0.1:8000/pages/`page-no`/?q=view-count
> *Dont forget to replace `<page-no>` by page-number example 1,2,3...
5. Endpoint to return posts in **paginated** `order by score`
GET http://127.0.0.1:8000/pages/`page-no`/?q=view-count
> *Dont forget to replace `<page-no>` by page-number example 1,2,3...
6. Display Answers endpoint
The Display answers endpoint is a very sophisticated endpoint having the following features:
- Display Answers based on question id having one or more answers.
>GET http://127.0.0.1:8000/answers/id/?id=11192
- Display Answers based on question id having no answers.
>GET http://127.0.0.1:8000/answers/id/?id=11485
```
{

"msg": "success",

"data": "No answers found"

}
```
- Handle question id which does not exist in database
> GET http://127.0.0.1:8000/answers/id/?id=1111 
```
{

"msg": "success",

"data": "No such questions found"

}
```
- Display Answers based on question title one or more answers.
>GET http://127.0.0.1:8000/answers/title/?title=Seurat FindMarkers() output, percentage
- Display Answers based on question title having no answers.
>GET http://127.0.0.1:8000/answers/title/?title=What are the different kinds of bioluminescent genes?
```
{

"msg": "success",

"data": "No answers found"

}
```
- Handle question titke which does not exist in database
> GET http://127.0.0.1:8000/answers/title/?title=this-question-doesnot-exist
```
{

"msg": "success",

"data": "No such questions found"

}
```
## Search Data Endpoints
1. Endpoint for Search by way of a query string which filters the posts based on the presence of the search term either in the title or body of the post.  
>GET http://127.0.0.1:8000/search/?q=`<string-to-search>`

Examples:
> http://127.0.0.1:8000/search/?q=wuhan

> http://127.0.0.1:8000/search/?q=wuh

> http://127.0.0.1:8000/search/?q=aaaaaaaaaaaa

> http://127.0.0.1:8000/search/?q=Why does the
2. **Elastic Smart Tokenized Search** 
Endpoint for Search by way of a query string which filters the posts based on the presence of the search term in `title` , `body` & `tags` by prebuilding indexers in elasticsearch and applying multiple tokenizers to enhance search result.
>GET http://127.0.0.1:9200/smart_search/search/?q=`<string-to-search>`

Examples:
> http://127.0.0.1:8000/search/?q=wuhan

> http://127.0.0.1:8000/search/?q=wuh

> http://127.0.0.1:8000/search/?q=aaaaaaaaaaaa

> http://127.0.0.1:8000/search/?q=Why does the
