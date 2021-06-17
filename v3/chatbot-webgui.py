#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash
from chatbot_ai import chatbot_ai

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Pa$$w0rd'


@app.route('/', methods=('GET', 'POST'))
def index():
    chatbot_label = "Hallo, worüber wollen Sie sprechen?"

    # Logik
    if request.method == 'POST':
        chatbot_input = request.form['chatbot_input']
        if not chatbot_input:
            flash("Ohne Frage kann ich nicht antworten")
        else:
            bot = chatbot_ai("v3/intents.json")
            bot.set_Message(chatbot_input)
            chatbot_label = bot.get_Response()

    return render_template('chatbot.html', chatbot_label=chatbot_label)
