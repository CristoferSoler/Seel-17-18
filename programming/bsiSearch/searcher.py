from whoosh.qparser import QueryParser
from whoosh.index import *

def exampleSearch():
    index = open_dir("index")
    with index.searcher() as searcher:
        query = QueryParser("content", index.schema).parse(sys.argv[1])
        results = searcher.search(query)

        if(len(results) != 0):
            print(results[0]['id'])
        else:
            print('No hints')

if __name__ == '__main__':
    exampleSearch()