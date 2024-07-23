import json
import logging
from flask import Flask, render_template
from post import Post
import requests

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Fetch and process blog posts
try:
    response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
    response.raise_for_status()  # Raise an exception for bad status codes
    posts_data = response.json()

    logger.info(f"Fetched data type: {type(posts_data)}")
    logger.info(f"Fetched data: {posts_data}")

    # Ensure posts_data is a list
    if isinstance(posts_data, dict):
        posts_data = [posts_data]
    elif isinstance(posts_data, str):
        posts_data = json.loads(posts_data)
        if isinstance(posts_data, dict):
            posts_data = [posts_data]

    post_objects = []
    for post in posts_data:
        try:
            post_obj = Post(post["id"], post["title"],
                            post["subtitle"], post["body"])
            post_objects.append(post_obj)
        except KeyError as e:
            logger.error(f"Missing key in post data: {e}")
        except Exception as e:
            logger.error(f"Error creating Post object: {e}")

    logger.info(f"Created {len(post_objects)} Post objects")

except requests.RequestException as e:
    logger.error(f"Error fetching data from API: {e}")
    post_objects = []

# Set up Flask application
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = next(
        (post for post in post_objects if post.id == index), None)
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
