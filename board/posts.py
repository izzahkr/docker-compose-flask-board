from flask import (
    Blueprint, redirect, render_template, request, url_for,
)
from board.database import get_pg_db_conn

bp = Blueprint("posts", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]

        if message:
            db = get_pg_db_conn()  # Get the database connection
            try:
                cur = db.cursor()  # Create a cursor from the connection
                cur.execute("INSERT INTO post (author, message) VALUES (%s, %s)", (author, message))
                db.commit()  # Commit the transaction
            except Exception as e:
                print(f"Error inserting post: {e}")
            finally:
                cur.close()  # Close the cursor
                db.close()  # Close the connection

            return redirect(url_for("posts.post"))
    
    return render_template("posts/create.html")

@bp.route("/posts")
def post():
    db = get_pg_db_conn()  # Get the database connection
    try:
        cur = db.cursor()  # Create a cursor from the connection
        cur.execute("SELECT author, message, created FROM post ORDER BY created DESC")
        posts = cur.fetchall()  # Fetch all the results
    except Exception as e:
        print(f"Error fetching posts: {e}")
        posts = []  # Fallback to an empty list if there's an error
    finally:
        cur.close()  # Close the cursor
        db.close()  # Close the connection
    
    return render_template("posts/posts.html", posts=posts)
