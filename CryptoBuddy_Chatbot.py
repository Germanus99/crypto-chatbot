
# 🤖 CryptoBuddy – Your AI Financial Sidekick

# 1. Greet the User
bot_name = "CryptoBuddy"

def greet():
    print(f"{bot_name}: Hey there! 👋 I'm {bot_name}, your AI crypto sidekick. Let’s find you a green 🌿 and growing 📈 coin!")

# 2. Predefined Crypto Data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# 3. Get user input
def get_user_query():
    return input("You: ").lower()

# 4. Advice Rules
def get_most_sustainable():
    best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    return f"{bot_name}: Invest in {best}! 🌱 It’s eco-friendly and has long-term potential!"

def get_most_profitable():
    candidates = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"]
    if candidates:
        return f"{bot_name}: {candidates[0]} is trending up 📈 and has strong market support. Great for short-term profits!"
    else:
        return f"{bot_name}: Hmm 🤔 I couldn't find a high-market coin that's rising right now."

def recommend_by_query(query):
    if "sustainable" in query:
        return get_most_sustainable()
    elif "profitable" in query or "profit" in query or "trending" in query:
        return get_most_profitable()
    elif "cardano" in query:
        return f"{bot_name}: Cardano (ADA) is trending up 🚀 and has a top-tier sustainability score of 8/10! 💚"
    elif "bitcoin" in query:
        return f"{bot_name}: Bitcoin is profitable 📈 but consumes a lot of energy ⚡. Invest with caution."
    elif "ethereum" in query:
        return f"{bot_name}: Ethereum is stable and has decent sustainability. A solid choice for balanced investors!"
    else:
        return f"{bot_name}: I'm not sure about that one. Try asking about sustainability, trends, or specific coins!"

# 5. Main Bot Loop
def chatbot():
    greet()
    print("Ask me things like: 'Which crypto is trending?', 'What’s the most sustainable coin?', or 'Tell me about Cardano'.")
    print("Type 'exit' to quit.\n")

    while True:
        query = get_user_query()
        if query == "exit":
            print(f"{bot_name}: Bye! 👋 Remember, crypto is risky—always DYOR (Do Your Own Research)!")
            break
        response = recommend_by_query(query)
        print(response)

# 6. Run the Bot
chatbot()
