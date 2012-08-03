# -*- coding: utf-8 -*-
from flaskext.wtf import Form, TextField, PasswordField, BooleanField, SelectMultipleField, validators, Required

class VoteForm(Form):
    name = TextField(u'工号(R000xx or W000xx):', validators=[Required(u'请输入工号')])
    password = PasswordField(u'密码:', validators=[Required(u'请输入密码')])
    #choice = RadioField(u'请投票:', choices=[('1', u'扬州'), ('2', u'上海欢乐谷'), ('3', u'南京'), ('4', u'溱潼')])
    first = BooleanField(u'扬州')
    second = BooleanField(u'上海欢乐谷')
    third = BooleanField(u'南京')
    fourth = BooleanField(u'溱潼')
    #choice = SelectMultipleField(u'请投票:', choices=[('1', u'扬州'), ('2', u'上海欢乐谷'), ('3', u'南京'), ('4', u'溱潼')])
