import matplotlib.pyplot as plt

# --------- Load dataset ---------
dataset = []
with open(r'C:\Users\ADMIN\Seq2SeqChatbot\dataset\chat_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if '|' in line:
            inp, out = line.strip().lower().split('|')
            dataset.append((inp, out))

# --------- Function to get reply ---------
def get_reply(user_input):
    user_input = user_input.lower()
    best_match = None
    max_overlap = 0
    overlaps = []

    for inp, reply in dataset:
        # Count how many words in user_input appear as substrings in dataset input
        overlap = sum(1 for word in user_input.split() if word in inp)
        overlaps.append(overlap)
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = reply

    # Plot overlap graph
    plt.clf()
    plt.bar(range(len(dataset)), overlaps, color='skyblue')
    plt.xticks(range(len(dataset)), [inp for inp, _ in dataset], rotation=45, ha='right')
    plt.ylabel('Number of matching words')
    plt.title('Keyword Matching with Dataset')
    plt.tight_layout()
    plt.pause(0.5)

    if max_overlap >= 1:  # reply if at least 1 match
        return best_match
    else:
        return "I am not sure how to reply to that."

# --------- Chat loop ---------
print("Chatbot: Hello! Type 'bye' to exit.")

plt.ion()
fig = plt.figure(figsize=(10,5))

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    reply = get_reply(user_input)
    print(f"Chatbot: {reply}")

plt.ioff()
plt.show()
