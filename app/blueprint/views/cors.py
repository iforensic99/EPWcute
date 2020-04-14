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

@admin.route("/cors")
def cors():
	return render_template("cors/cors.html",PocText="")

@admin.route("/corsHandler",methods=["GET", "POST"])
def corsHandler():
	getPoc = '''
	    <script type="text/javascript">
        var req = new XMLHttpRequest();
        req.onload = reqListener;
        req.open('get', '{0}', true);
        //req.setRequestHeader("Content-Type","application/x-www-form-urlencoded;"); 
        req.withCredentials = true;
        req.send();

        function reqListener() {{
            var output = document.getElementById('output');
            output.innerHTML = "URL:{0}<br><br>Response:<br><textarea style='width: 659px; height: 193px;'>" + req.responseText + "</textarea>";
        }};
    </script>
	
	'''

	postPoc = '''
		<script type="text/javascript">
        var req = new XMLHttpRequest();
        var data = "{1}";
        req.onload = reqListener;
        req.open('post', '{0}', true);
        req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        req.withCredentials = true;
        req.send(data);

        function reqListener() {{
            var output = document.getElementById('output');
            output.innerHTML = "URL: {0}<br>Data: {1}<br><br>Response:<br><textarea style='width: 659px; height: 193px;'>" + req.responseText + "</textarea>";
        }};
    </script>
	'''



	if request.method == "GET":
		url = request.args.get('url', None)
		data = request.args.get('data', None)
		method = request.args.get('method',None)
		dotest = request.args.get("test",None)

		datas = {"url":url,"data":data}
		if method == "get":
			if dotest == "true":
				return render_template("cors/cors_get.html",datas=datas)
			poctext=getPoc.format(url)
			return render_template("cors/cors.html",PocText=poctext)
		elif method == "post":
			if dotest == "true":
				return render_template("cors/cors_post.html",datas=datas)
			poctext = postPoc.format(url,data)
			return render_template("cors/cors.html",PocText=poctext)
    		
	return "error"	