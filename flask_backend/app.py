from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/search', methods=['POST'])
@cross_origin()
def hello():

    ix = open_dir("../final_data/indexdir")
 
    with ix.searcher(weighting=scoring.Frequency) as searcher:
        query = QueryParser("lyrics", ix.schema).parse(request.json['term'])
        results = searcher.search(query,limit=10)
        returned = []
        for i in range(min(len(results), 10)):
            returned.append({
                'id': results[i]['id'],
                'lyrics': results[i]['lyrics'],
                'song_name': results[i]['song_name'],
                'angry_score': results[i]['angry_score'],
                'happy_score': results[i]['happy_score'],
                'relaxed_score': results[i]['relaxed_score'],
                'sad_score': results[i]['sad_score'],
                'author': results[i]['author']
            })
        return json.dumps(returned)

if __name__ == '__main__':
    app.run()