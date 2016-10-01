from flask import render_template

from .blueprint import blueprint

__all__ = ['bookmark_index']

@blueprint.route('/')
def bookmark_index():
    return render_template('bookmark/index.html')