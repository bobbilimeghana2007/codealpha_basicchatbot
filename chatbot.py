from datetime import datetime
import random

# Stylish Heading
print("╔══════════════════════════════════════╗")
print("║     🤖 SMART PYTHON CHATBOT 🤖      ║")
print("║      CodeAlpha Internship Task      ║")
print("╚══════════════════════════════════════╝")

print("\n✨ Type 'help' to see available commands.")
print("✨ Type 'bye' to exit the chatbot.\n")

# Ask user name
user_name = input("👤 Enter your name: ")

# Motivational Quotes
motivations = [
    "🌟 Believe in yourself. You can do amazing things!",
    "🚀 Every expert was once a beginner.",
    "💪 Success comes from consistency.",
    "📚 Study hard today for a better tomorrow.",
    "🔥 Never stop learning and improving."
]

# Jokes List
jokes = [
    "😂 Why do programmers prefer Python? Because it's easy to understand!",
    "😂 Why was the computer cold? Because it forgot to close Windows!",
    "😂 Why did the Python developer go broke? Because he used too many loops!",
    "😂 Why do programmers hate nature? Too many bugs!"
]

# Study Tips
study_tips = [
    "📖 Study for 45 minutes and take a short break.",
    "📝 Make handwritten notes while learning.",
    "🎯 Practice coding daily to improve logic.",
    "💡 Revise important concepts regularly.",
    "📚 Focus on understanding instead of memorizing."
]

# Open Chat History File with UTF-8 Encoding
file = open("chat_history.txt", "a", encoding="utf-8")

# Save Session Start
file.write(f"\n--- Chat Session with {user_name} ---\n")

# Main Chatbot Loop
while True:

    # User Input
    user_input = input(f"\n👤 {user_name}: ").lower()

    # Save User Input
    file.write(f"{user_name}: {user_input}\n")

    # Greeting Responses
    if user_input in ["hello", "hi", "hey"]:
        response = f"👋 Hello {user_name}! Nice to meet you."

    # How Are You
    elif user_input == "how are you":
        response = "😊 I am doing great! Ready to help you."

    # Bot Name
    elif user_input == "what is your name":
        response = "🤖 I am Smart Python Chatbot created by Meghana."

    # Time Feature
    elif user_input == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        response = f"⏰ Current time is {current_time}"

    # Date Feature
    elif user_input == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        response = f"📅 Today's date is {current_date}"

    # Joke Feature
    elif user_input == "joke":
        response = random.choice(jokes)

    # Motivation Feature
    elif user_input == "motivate me":
        response = random.choice(motivations)

    # Study Tips Feature
    elif user_input == "study tips":
        response = random.choice(study_tips)

    # Python Information
    elif user_input == "python":
        response = "🐍 Python is a beginner-friendly programming language used in AI, Web Development, Data Science, and Automation."

    # Internship Guidance
    elif user_input == "internship":
        response = "💼 Internships help improve skills, build projects, and strengthen your resume."

    # Career Guidance
    elif user_input == "career":
        response = "🚀 Keep learning programming, build projects, use GitHub, and stay active on LinkedIn."

    # Thank You Response
    elif user_input in ["thanks", "thank you"]:
        response = "💖 You're welcome! Happy coding."

    # Help Command
    elif user_input == "help":
        response = """
📌 Available Commands:
🔹 hello / hi / hey
🔹 how are you
🔹 what is your name
🔹 time
🔹 date
🔹 joke
🔹 motivate me
🔹 study tips
🔹 python
🔹 internship
🔹 career
🔹 thanks
🔹 bye
"""

    # Exit Command
    elif user_input == "bye":
        response = f"👋 Goodbye {user_name}! Have a wonderful day."

        print("\n🤖 Bot:", response)

        file.write(f"Bot: {response}\n")
        break

    # Unknown Commands
    else:
        response = "❌ Sorry, I don't understand that command. Type 'help' to see available commands."

    # Print Bot Response
    print("\n🤖 Bot:", response)

    # Save Bot Response
    file.write(f"Bot: {response}\n")

# Close File
file.close()

print("\n💾 Chat history saved successfully in 'chat_history.txt'")
print("✨ Thank you for using Smart Python Chatbot ✨")