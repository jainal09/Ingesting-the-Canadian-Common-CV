# Steps to add to docker-hub
> (For personal use)
```dockerfile
docker build -t ingesting_common_cv:latest .

docker tag ingesting_common_cv:latest jainal09/ingesting_common_cv:l
atest

docker push jainal09/ingesting_common_cv:latest
```
