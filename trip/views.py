# -*- coding: utf-8 -*-

from trip import app
from trip.forms import VoteForm
from trip.models import db, Vote
from flask import render_template, redirect, url_for, request
import ldap
from sqlalchemy import func

places = {1:u'扬州', 2:u'上海欢乐谷', 3:u'南京', 4:u'溱潼'}

@app.route('/', methods=['GET'])
@app.route('/vote', methods=['POST'])
def home():
    form = VoteForm(csrf_enabled=False)
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data.upper()
        password = form.password.data
        #choice = int(form.choice.data)
        if do_auth(name, password):
            vote_in_db = Vote.query.filter(Vote.name==name).first()
            if vote_in_db:
                form.name.errors.append(u'该工号已投票')
                return render_template('index.html', form=form)
            else:
                first = form.first.data
                second = form.second.data
                third = form.third.data
                fourth = form.fourth.data
                choices = []
                if first:
                    choices.append(1)
                if second:
                    choices.append(2)
                if third:
                    choices.append(3)
                if fourth:
                    choices.append(4)
                if len(choices) > 2 or len(choices) < 1:
                    form.first.errors.append(u'请选择一或两项')
                    return render_template('index.html', form=form)
                for choice in choices:
                    vote = Vote(name=name,choice=choice,ip=request.remote_addr)
                    db.session.add(vote)
                db.session.commit()
        else:
            form.name.errors.append(u'工号或者密码错误')
            return render_template('index.html', form=form)

        return redirect(url_for('result'))
    else:
        if form.errors:
            print form.errors
        return render_template('index.html', form=form)

@app.route('/result')
def result():
    choices = db.session.query(Vote.choice, func.count(Vote.id).label('number')).group_by(Vote.choice)
    results = []
    sum = 0
    for c in choices:
        r = {}
        r['place'] = places[c.choice]
        r['votes'] = c.number
        sum += c.number
        results.append(r)
    for r in results:
        r['percent'] = r['votes'] * 100.0 / sum
    return render_template('result.html', results=results, sum=sum)


def do_auth(username, password):
    try:
        l = ldap.initialize('ldap://172.25.5.211:389')
        dn = 'cn=%s,ou=withmail,ou=zycn,dc=zyxel,dc=com' % username
        if l.simple_bind_s(dn, password):
            l.unbind()
            return True
        else:
            return False
    except ldap.LDAPError, e:
        print e
        return False
