import random
import json

menu_items = ["Big Mac", "Cheeseburger", "Quarter Pounder with Cheese", "Quarter Pounder with Cheese Deluxe", "McDouble", "Kane's box 3 finger", "Kane's box 4 finger", "Kane's box 6 finger", "Cheese Pizza", "Pepperoni Pizza"]

def generate_edge_cases_order():
    item = random.choice(menu_items)
    conversation = []
    data = []
    
    # Initial order
    conversation.append(("I would like to order a {}.".format(item), "Would you like anything else with your {}?".format(item)))
    
    # Adding an item
    another_item = random.choice([i for i in menu_items if i != item])
    conversation.append(("I would also like a {}.".format(another_item), "Got it. Anything else?"))
    
    # Removing the item
    conversation.append(("Actually, remove the {}.".format(another_item), "Okay, removed the {}. Anything else?".format(another_item)))
    
    # Changing the order
    new_item = random.choice([i for i in menu_items if i != item and i != another_item])
    conversation.append(("I would like to change my order to a {}.".format(new_item), "Sure, changed to a {}. Anything else?".format(new_item)))
    
    conversation.append(("No, that's all.", "Sure, a {}. Your total is [TOTAL_AMOUNT]. Is that correct?".format(new_item)))
    
    for i in range(len(conversation) - 1):
        data.append({
            'input_text': conversation[i][0],
            'response_text': conversation[i][1]
        })
    
    return data

def generate_edge_cases_dataset(num_conversations):
    dataset = []
    for _ in range(num_conversations):
        dataset.extend(generate_edge_cases_order())
    return dataset

def save_dataset(dataset, filename):
    with open(filename, 'w') as f:
        json.dump(dataset, f, indent=4)

# Generate and save the dataset
num_conversations = 500  # Adjust the number of conversations as needed
dataset = generate_edge_cases_dataset(num_conversations)
save_dataset(dataset, 'edge_cases_order_data.json')
