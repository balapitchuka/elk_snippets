from elasticsearch import Elasticsearch
client = Elasticsearch("http://localhost:9200/")
resp = client.info()
print(resp)