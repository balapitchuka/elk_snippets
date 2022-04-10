from elasticsearch import Elasticsearch
client = Elasticsearch("http://localhost:9200/")
   
def select_data_from_elastic(index='test_index',doc_type='employee',id=3):    
    res=client.get(index=index,doc_type=doc_type,id=id)
    print (res) 
        
if __name__ == "__main__":
    select_data_from_elastic()