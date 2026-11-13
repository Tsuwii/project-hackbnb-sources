from flask import Blueprint, request, abort, request, send_from_directory
from werkzeug.utils import secure_filename
import os

uploads_api = Blueprint('uploads', __name__)

@uploads_api.route('/')
def get_upload():
   filename = secure_filename(request.args.get("name", ""))
   if os.path.splitext(filename)[1].lower() not in {'.jpg', '.jpeg', '.png', '.webp'}:
      abort(404)
   return send_from_directory('uploads', filename)
 