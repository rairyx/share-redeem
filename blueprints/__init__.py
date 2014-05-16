import os.path

from lib import import_dir
from flask import Blueprint, render_template, abort

index_page = Blueprint('index_page', __name__,
                        template_folder='../templates')

__current_dir = os.path.abspath(__name__)
import_dir(__current_dir)
