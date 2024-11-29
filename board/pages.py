from flask import Blueprint, render_template, request, redirect, url_for
from board.database import get_db

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route("/posts")
def posts():
    db = get_db()  # Get the database connection
    try:
        cur = db.cursor()  # Create a cursor from the connection
        cur.execute("SELECT author, message, created FROM post ORDER BY created DESC")  # Specify columns
        posts = cur.fetchall()  # Fetch all results from the cursor
        print(f"Fetched posts: {posts}")  # Debug print
    except Exception as e:
        print(f"Error fetching posts: {e}")
        posts = []  # Fallback to an empty list if there's an error
    finally:
        cur.close()  # Always close the cursor
        db.close()  # Always close the connection
    
    return render_template("posts/posts.html", posts=posts)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]

        if message:
            db = get_db()
            try:
                cur = db.cursor()
                cur.execute("INSERT INTO post (author, message) VALUES (%s, %s)", (author, message))
                db.commit()
            except Exception as e:
                print(f"Error inserting post: {e}")  # Debugging jika ada error saat insert
            finally:
                cur.close()
                db.close()

            return redirect(url_for("pages.posts"))  # Ubah ke pages.posts

    return render_template("posts/create.html")
