import random
import json

menu_items = ["Big Mac", "Cheeseburger", "Quarter Pounder with Cheese", "Quarter Pounder with Cheese Deluxe", "McDouble", "Kane's box 3 finger", "Kane's box 4 finger", "Kane's box 6 finger", "Cheese Pizza", "Pepperoni Pizza"]

def generate_multiple_items_order():
    num_items = random.randint(2, 4)  # Number of items in the order
    items = random.sample(menu_items, num_items)
    conversation = []
    data = []
    
    # Initial order
    conversation.append(("I would like to order a {}.".format(items[0]), "Would you like anything else with your {}?".format(items[0])))
    
    for item in items[1:]:
        conversation.append(("I would also like a {}.".format(item), "Got it. Anything else?"))
    
    conversation.append(("No, that's all.", "Sure, {}. Can I have your name for the order?".format(", ".join(items))))
    conversation.append(("My name is John.", "Thank you, John. Your total is [TOTAL_AMOUNT]. Is that correct?"))
    
    for i in range(len(conversation) - 1):
        data.append({
            'input_text': conversation[i][0],
            'response_text': conversation[i][1]
        })
    
    return data

def generate_multiple_items_dataset(num_conversations):
    dataset = []
    for _ in range(num_conversations):
        dataset.extend(generate_multiple_items_order())
    return dataset

def save_dataset(dataset, filename):
    with open(filename, 'w') as f:
        json.dump(dataset, f, indent=4)

# Generate and save the dataset
num_conversations = 100  # Adjust the number of conversations as needed
dataset = generate_multiple_items_dataset(num_conversations)
save_dataset(dataset, 'multiple_items_order_data_with_name.json')
