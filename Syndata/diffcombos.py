import random
import json

menu_items_with_customizations = {
    "Big Mac": ["no pickles", "extra cheese", "no onions"],
    "Cheeseburger": ["no ketchup", "extra cheese", "no onions"],
    "Quarter Pounder with Cheese": ["extra patty", "no pickles", "extra cheese"],
    "Quarter Pounder with Cheese Deluxe": ["no pickles", "extra patty", "extra cheese"],
    "McDouble": ["no onions", "extra cheese", "no ketchup"],
    "Kane's box 3 finger": ["extra sauce", "extra chicken tender", "extra toast"],
    "Kane's box 4 finger": ["extra sauce", "extra chicken tender", "extra toast"],
    "Kane's box 6 finger": ["extra sauce", "extra chicken tender", "extra toast"],
    "Cheese Pizza": ["extra cheese", "onions", "no cheese"],
    "Pepperoni Pizza": ["extra cheese", "onions", "no cheese"]
}

drinks = ["Coke", "Sprite", "Dr. Pepper", "lemonade", "pink lemonade"]

def generate_customizations_order():
    item = random.choice(list(menu_items_with_customizations.keys()))
    customizations = random.sample(menu_items_with_customizations[item], random.randint(1, 3))
    drink = random.choice(drinks)
    conversation = []
    data = []
    
    # Initial order
    conversation.append(("I would like to order a {}.".format(item), "Would you like anything else with your {}?".format(item)))
    
    for customization in customizations:
        conversation.append(("Yes, add {}.".format(customization), "Got it. Anything else?"))
    
    conversation.append(("A {}, please.".format(drink), "Sure, a {} with {} and a {}. Your total is [TOTAL_AMOUNT]. Is that correct?".format(item, ", ".join(customizations), drink)))
    
    conversation.append(("Yes.", "Thank you! Please proceed to the payment window."))
    
    for i in range(len(conversation) - 1):
        data.append({
            'input_text': conversation[i][0],
            'response_text': conversation[i][1]
        })
    
    return data

def generate_customizations_dataset(num_conversations):
    dataset = []
    for _ in range(num_conversations):
        dataset.extend(generate_customizations_order())
    return dataset

def save_dataset(dataset, filename):
    with open(filename, 'w') as f:
        json.dump(dataset, f, indent=4)

# Generate and save the dataset
num_conversations = 500  # Adjust the number of conversations as needed
dataset = generate_customizations_dataset(num_conversations)
save_dataset(dataset, 'customizations_order_data.json')
