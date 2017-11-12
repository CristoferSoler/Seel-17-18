from whoosh.fields import *
from whoosh.index import *

def createSchema():
    return Schema(id=TEXT(stored=True), content=TEXT)

def createIndex(schema):
    if not os.path.exists("index"):
        os.mkdir("index")
    index = create_in("index", schema)
    writer = index.writer()
    writer.add_document(id=u"B 1.0", content="Hackerangriff ist ein bisschen gefaehrlich")
    writer.add_document(id=u"B 1.1", content="Fishing ist ein bisschen gefaehrlich")
    writer.commit()
    print('Indexing is finished')

if __name__ == '__main__':
    schema = createSchema()
    createIndex(schema)