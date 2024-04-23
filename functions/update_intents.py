from functions.io import load_data_from_csv, save_data_to_csv
from functions.logger import create_logger

data = load_data_from_csv("data/clean/updated_final_clean_data_yes_no.csv")

logger = create_logger()

# 653


def update(data, new_intent_name):
    # GOAL: Update the intents in the data THAT THE USER APPROVES OF

    for i in range(len(data)):
        # Get the intent
        text = data.loc[i, "text"]
        intent = data.loc[i, "intent"]

        logger.text(f"Text: {text}")
        logger.intent(f"Intent: {intent}")

        # Ask the user if they want to update the intent
        user_input = input("Do you want to update this intent? (y/n): ")
        user_input = user_input or "n"
        user_input = user_input.lower()

        if user_input == "y":
            # Update the intent
            data.loc[i, "intent"] = new_intent_name
            logger.intent(f"Updated Intent: {new_intent_name}")
        elif user_input == "q":
            save_data_to_csv(data, "data/clean/updated_data.csv")
            break

    return data


new_intent_name = "call_back_later_intent"
updated_data = update(data, new_intent_name)
print(updated_data.head())

# Save the updated data
save_data_to_csv(updated_data, "data/clean/updated_data.csv")
