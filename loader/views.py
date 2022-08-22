from flask import Blueprint, render_template, request, send_from_directory
from utils import add_post, is_filename_allowed
import logging

logging.basicConfig(level=logging.INFO)
loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route("/post", methods=["GET"])
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    content = request.form['content']
    path = r'C:/Users/andre/Desktop/Skypro/Homework12/uploads/images'+f'/{picture.filename}'
    url = r'uploads/images'+f'/{picture.filename}'
    if is_filename_allowed(picture.filename):
        picture.save(url)
    else:
        logging.info("Загруженный файл - не картинка")
        extension = picture.filename.split(".")[-1]
        return f"<h1>Ошибка загрузки</h1>"
    if add_post(url,  content):
        return render_template('post_uploaded.html', picture=url, content=content)
    else:
        logging.error("Ошибка при загрузке файла")
        return f"<h1>Ошибка загрузки</h1>"
