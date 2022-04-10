from elasticsearch import Elasticsearch
client = Elasticsearch("http://localhost:9200/")

def send_data_to_elastic():
    e1={
        "first_name":"Donald",
        "last_name":"Trump",
        "age": 65,
        "about": "Love to play beyzboll",
        "interests": ['sports','music'],
    }
    print(e1)
    client.index(index='test_index',doc_type='employee',id=3,body=e1) 
        
if __name__ == "__main__":
    send_data_to_elastic()