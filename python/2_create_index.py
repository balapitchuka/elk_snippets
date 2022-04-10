from elasticsearch import Elasticsearch
client = Elasticsearch("http://localhost:9200/")

def create_index(index_name):
    if not client.indices.exists(index_name):
        client.indices.create(index=index_name)
        print(index_name+" index is created")
    else:
        print(index_name+" already exist")
        
if __name__ == "__main__":
    create_index("test_index")