import openai

def get_chatbot_reply(user_msg):
    user_msg = user_msg.lower()

    # Rule-based quick tips
    if "save" in user_msg:
        return "Try saving at least 20% of your income."
    if "overspend" in user_msg or "budget" in user_msg:
        return "Cut down on non-essential categories like dining or shopping."
    if "food" in user_msg:
        return "Maybe set a weekly food budget to control overspending."

    # Optional AI (requires API key)
    try:
        openai.api_key = "YOUR_OPENAI_KEY"
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=user_msg,
            max_tokens=60
        )
        return response.choices[0].text.strip()
    except:
        return "Basic advice: Spend less than you earn and save first!"
