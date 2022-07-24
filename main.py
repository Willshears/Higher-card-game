
# make a deck of cards
import random
values = range(2, 15)
suits = "D C H S".split()

deck = ["{0}{1}".format(v, s) for v in values for s in suits]
print(deck)
print(len(deck))
monte_carlo = 10000000
card_draws = 4
instances = 0
evaluator = 0
for hand in range(monte_carlo):
    previous_cards = []
    deck_instance = deck
    fresh_card = random.choice(deck_instance)
    multiplier = 0
    for round in range(card_draws):
        print(round)
        last_card = fresh_card
        previous_cards.append(last_card)
        if last_card:
            fresh_card = random.choice(deck_instance)
            while fresh_card in previous_cards:
                # print(previous_cards)
                # print("Card already used:")
                # print(fresh_card)
                fresh_card = random.choice(deck_instance)
                # print("New card:")
                # print(fresh_card)
        if last_card[:-1] < fresh_card[:-1]:
            multiplier += 1
            if multiplier == 4:
                evaluator +=1
    instances +=1
print(f"Percentage of time better cards draw x5:    % {evaluator / instances * 100}")

