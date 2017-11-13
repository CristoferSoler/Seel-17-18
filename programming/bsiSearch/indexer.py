from whoosh.fields import *
from whoosh.index import *
from whoosh.analysis import *

def createSchema():
    return Schema(id=TEXT(stored=True), content=TEXT)

def createIndex(schema):
    if not os.path.exists("index"):
        os.mkdir("index")
    index = create_in("index", schema)

    firstDocument = "testing is bad"
    secoundDocument= "Fishing ist ein bisschen gefaehrlich"

    my_analyzer = StemmingAnalyzer()
    preProcessedText = [token.text for token in my_analyzer(firstDocument)]

    writer = index.writer()
    writer.add_document(id=u"B 1.0", content=preProcessedText)
    #writer.add_document(id=u"B 1.1", content=)
    writer.commit()
    print('Indexing is finished')

if __name__ == '__main__':
    schema = createSchema()
    createIndex(schema)