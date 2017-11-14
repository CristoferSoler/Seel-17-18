from whoosh.fields import *
from whoosh.index import *
from whoosh.analysis import *
import json

def clearIndex(index):
    create_in(index)

def createSchema():
    return Schema(id=TEXT(stored=True), content=TEXT(analyzer=StemmingAnalyzer()))

def deleteDocumentByID(id,index):
    if os.path.exists(index):
        index.delte_by_term('id',id)
        index.commit()

def createIndex(schema):

    directory = '/Users/Jonathan/PycharmProjects/Seel-17-18/programming/bsiCrawler/content'

    if not os.path.exists("index"):
        os.mkdir("index")
    index = create_in("index", schema)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.json'):
           with open(directory + "/" + file) as fileOpen:
               jsonFile = json.load(fileOpen)
               wholeText = jsonFile['wholeText']
               headline = jsonFile['h1']
               id = " ".join(headline.split(" ",2)[:2])
               writer = index.writer()

               writer.add_document(id=id, content=wholeText)
               writer.commit()

        else:
            continue

    print('Indexing is finished')

if __name__ == '__main__':
    schema = createSchema()
    createIndex(schema)
