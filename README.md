Check local
```
docker run -p 8000:8000 \
  -e CONSUMER_KEY=  \
  -e CONSUMER_SECRET= \
  -e TOKEN= \
  -e TOKEN_SECRET= \
  bricklink-api:latest
```
endpoint to http request
```
http://bricklink-api.n8n.svc.cluster.local:8000
```