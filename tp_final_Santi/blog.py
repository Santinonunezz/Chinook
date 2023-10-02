from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    canciones = db.execute(
        """SELECT t.name as cancion,g.name as genero,ar.name as artista,mt.name as formato,a.title
        FROM tracks t JOIN albumb a ON t.AlbumId = a.AlbumId
        JOIN genres g ON g.GenreId = t.GenreId
        JOIN artists ar ON ar.ArtistId = a.ArtistId
        JOIN media_types mt ON mt.MediaTypeId = t.MediaTypeId"""
    ).fetchall()
    return render_template('blog/index.html', canciones=canciones)

