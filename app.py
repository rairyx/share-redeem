# -*- coding: utf-8 -*-
from blueprints import *
from prize import *
from flask import Flask, make_response,request,Response, session, g, redirect, url_for, abort, \
    render_template, flash, _app_ctx_stack,stream_with_context

app = Flask(__name__)
app.register_blueprint(index_page)
app.register_blueprint(redeem, url_prefix='/redeem')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5004)
  #  app.run(debug=True,host='0.0.0.0')
