from elasticsearch import Elasticsearch
client = Elasticsearch("http://localhost:9200/")

def search():
    res= client.search(index='test_index',body={'query':{'match_all':{}}})
    print('Got hits:', res['hits']['total']['value'])
    print(res['hits']['hits'])
    # Got hits: 1
    # [{'_index': 'test_index', '_type': 'employee', '_id': '3', '_score': 1.0, '_source': {'first_name': 'Donald', 'last_name': 'Trump', 'age': 65, 'about': 'Love to play beyzboll', 'interests': ['sports', 'music']}}]

    res= client.search(index='test_index',body={'query':{'match':{'first_name':'Donald'}}})
    print(res['hits']['hits'])
    # [{'_index': 'test_index', '_type': 'employee', '_id': '3', '_score': 0.2876821, '_source': {'first_name': 'Donald', 'last_name': 'Trump', 'age': 65, 'about': 'Love to play beyzboll', 'interests': ['sports', 'music']}}]

def search_bool():
    res= client.search(index='test_index',body={
            'query':{
                'bool':{
                    'must':[{
                            'match':{
                                'first_name':'Donald'
                            }
                        }]
                }
            }
        })
    print(res['hits']['hits'])
    # [{'_index': 'test_index', '_type': 'employee', '_id': '3', '_score': 0.2876821, '_source': {'first_name': 'Donald', 'last_name': 'Trump', 'age': 65, 'about': 'Love to play beyzboll', 'interests': ['sports', 'music']}}]
    
def search_filter():
    res= client.search(index='test_index',body={
            'query':{
                'bool':{
                    'must':{
                        'match':{
                            'first_name':'Donald'
                        }
                    },
                    "filter":{
                        "range":{
                            "age":{
                                "gt":27
                            }
                        }
                    }
                }
            }
        })
    print(res['hits']['hits'])
    # [{'_index': 'test_index', '_type': 'employee', '_id': '3', '_score': 0.2876821, '_source': {'first_name': 'Donald', 'last_name': 'Trump', 'age': 65, 'about': 'Love to play beyzboll', 'interests': ['sports', 'music']}}]
    
def search_match():
    res= client.search(index='test_index',doc_type='employee',body={
            'query':{
                'match':{
                    "about":"play cricket"
                }
            }
        })
    for hit in res['hits']['hits']:
        print(hit['_source']['about'])
        print(hit['_score'])
        
    # Love to play beyzboll
    # 0.2876821

def delete_data_from_elastic(index='test_index',doc_type='employee',id=3):    
    res=client.delete(index=index,doc_type=doc_type,id=id)
    print (res)
    # {'_index': 'test_index', '_type': 'employee', '_id': '3', '_version': 2, 'result': 'deleted', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 1, '_primary_term': 1}

    
def get_index_count():
    res= client.search(index="test_index",body={'query':{'match_all':{}}})
    print('Index count: ', res['hits']['total']['value']) 
    # Index count:  1
        
  
# kibana GET /_cat/indices/
# python print(es.cat.indices())

# kibana GET /_cat/health
# python print(es.cat.health())
  
if __name__ == "__main__":
    search()
    search_bool()
    search_filter()
    full_text_search()
    delete_data_from_elastic()
    get_index_count()