from flask import Blueprint, request, jsonify
from models import session, Income, Expense, Savings
from chatbot import get_chatbot_reply

api = Blueprint("api", __name__)

@api.route("/income", methods=["POST"])
def add_income():
    data = request.json
    income = Income(amount=data["amount"])
    session.add(income)
    session.commit()
    return jsonify({"message": "Income added"})

@api.route("/expense", methods=["POST"])
def add_expense():
    data = request.json
    expense = Expense(category=data["category"], amount=data["amount"])
    session.add(expense)
    session.commit()
    return jsonify({"message": "Expense added"})

@api.route("/savings", methods=["POST"])
def set_savings():
    data = request.json
    savings = Savings(goal=data["goal"])
    session.add(savings)
    session.commit()
    return jsonify({"message": "Savings set"})

@api.route("/chatbot", methods=["POST"])
def chatbot():
    user_msg = request.json["message"]
    reply = get_chatbot_reply(user_msg)
    return jsonify({"reply": reply})
