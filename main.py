from flask import Flask

from utils import get_candidates, format_candidates

app = Flask(__name__)


@app.route('/')
def main():
    candidates_list = get_candidates('candidates.json')

    return format_candidates(candidates_list)


@app.route('/candidates/<candidate_id>')
def page_candidate(candidate_id):
    pass


@app.route('/skills/<skill_id>')
def skills(skill_id):
    pass


app.run()
