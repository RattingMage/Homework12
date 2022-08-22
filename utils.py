import json

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def is_filename_allowed(filename):
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


def load_json():
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def search_post(word):
    posts = load_json()
    result = []
    for post in posts:
        content = post['content'].lower().split()
        if word in content:
            result.append(post)
    return result


def add_post(path, text):
    try:
        posts = load_json()
        posts.append({
            "pic": path,
            "content": text
        })
        with open('posts.json', mode='w', encoding='utf-8') as file:
            json.dump(posts, file, ensure_ascii=False)
        return True
    except:
        return False
