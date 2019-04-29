
from flask import Blueprint, request, render_template,\
    redirect, url_for
from back.models import Article


web_blueprint = Blueprint('web', __name__)

@web_blueprint.route('/index/',methods=['GET','POST'])
def index():
    articles=Article.query.limit(14).all()

    return render_template('web/index.html',articles=articles)


@web_blueprint.route('/info/<int:id>/',methods=['GET','POST'])
def info(id):
    article=Article.query.get(id)
    return render_template('web/info.html',article=article)
























































# @web_blueprint.route('/about/',methods=['GET','POST'])
# def about():
#     return render_template('web/about.html')
#
# @web_blueprint.route('/gbook/',methods=['GET','POST'])
# def gbook():
#     return render_template('web/gbook.html')
#
#
#
# @web_blueprint.route('/infopic/',methods=['GET','POST'])
# def infopic():
#     return render_template('web/infopic.html')
#
# @web_blueprint.route('/list/',methods=['GET','POST'])
# def list():
#     return render_template('web/list.html')
#
# @web_blueprint.route('/share/',methods=['GET','POST'])
# def share():
#     return render_template('web/share.html')