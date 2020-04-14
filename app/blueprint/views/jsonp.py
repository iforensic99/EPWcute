import math
import datetime


from flask import render_template
from flask import request
from flask import jsonify
from flask import session

from app.blueprint import admin
from app.blueprint import admin_required
from app.lib.utils.tools import get_page
from app.lib.utils.tools import get_uuid
from app.lib.utils.tools import json_to_excel
from app.lib.core.agent import Controller
from app.extensions import mongo

@admin.route("/jsonp")
def jsonp():
	return render_template("jsonp/jsonp.html")

@admin.route("/jsonp_test",methods=["GET", "POST"])
def jsonp_test():
	if request.method == "GET":
		url = request.args.get('url',None)
		cvalue = request.args.get('cvalue',None)
		txt = '<script>function %s(data){ alert(JSON.stringify(data)) }</script> <script src="%s"></script>'%(cvalue,url)
		return render_template("jsonp/jsonp.html",pocText=txt)