from flask import Blueprint, render_template, request
from utils import search_post
import logging

logging.basicConfig(level=logging.INFO)

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route("/")
def page_index():
    return render_template('index.html')


@main_blueprint.route("/search")
def search_page():
    logging.info("Выполнен поиск")
    s = request.args['s']
    posts = search_post(s.lower())
    return render_template('post_list.html', s=s, posts=posts)

