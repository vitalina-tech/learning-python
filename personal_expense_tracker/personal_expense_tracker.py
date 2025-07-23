name = input("Hello, enter your name:")

GREEN='\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def get_choice_input(prompt, min_val=None, max_val=None):
    while True:
        choice = input(prompt)
        if choice.lower() == 'done':
            return 'done'
        try:
            value = int(choice)
            if min_val is not None and value < min_val:
                print(f"Please enter a number >= {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Please enter a number <= {max_val}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number or 'done'.")

budget = get_choice_input("Enter your daily budget: ", min_val=0)

all_buy=[]

while True:
    item = input("Enter item name:")
    if item == "done":
        break
    spent=get_choice_input("Enter amount spent: ", min_val = 0)
    if spent == 'done':
        break
    category = input("Enter category:")
    if category == 'done':
        break
    buy = (item, spent, category)
    all_buy.append(buy)

while all_buy:
     print("\nYour purchases list:")
     for i, buy in enumerate(all_buy, 1):
          print(f"{i}. {buy[0].capitalize()} ${buy[1]} ({buy[2]})")
     print("\nDo you want to remove something?")
     remove = get_choice_input("Please enter the number of buy to remove or 'done' to finish: ", min_val = 1, max_val = len(all_buy))
     if remove == 'done':
          break
     all_buy.pop(remove - 1)

total_spent=sum(buy[1] for buy in all_buy)
print(f"Total spent is {total_spent}$")

if total_spent <= budget:
    print(f"{GREEN}{budget-total_spent}$ left in budget.{RESET}")
else:
    print(f"{RED}{total_spent-budget}$ over budget.{RESET}")

print(f"{total_spent/budget*100:.1f}% of budget used.")


all_categories = set(buy[2] for buy in all_buy)
all_cat_spent=[]
for cat in all_categories:
    cat_total_spent=sum(buy[1] for buy in all_buy if buy[2] == cat)
    all_cat_spent.append(cat_total_spent)

print("Spending by category:")

for cat in zip(all_categories, all_cat_spent):
    print(f"{cat[0]}: {cat[1]}$")

highest_spent=max(buy[1] for buy in all_buy)
expensive_buy=[buy[0] for buy in all_buy if buy[1]==highest_spent]

print(f"Most expensive purchase:")
for item in expensive_buy:
    print(f"{item} {highest_spent}$")
