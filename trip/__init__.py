# -*- coding: utf-8 -*-
from flask import Flask
import settings

app = Flask("trip")
app.config.from_object("trip.settings")

import views

