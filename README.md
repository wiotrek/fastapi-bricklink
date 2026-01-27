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
k8s secrets
```
kubectl create secret generic bricklink-secrets \
  -n n8n \
  --from-literal=consumer_key= \
  --from-literal=consumer_secret= \
  --from-literal=token= \
  --from-literal=token_secret=
```