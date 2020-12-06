from replit import clear
#HINT: You can call clear() to clear the output in the console.
next_player = True
bidders_data=[]

def add_bidders_data(name,bid):
    bidders_data.append({
        'name':name,
        'bid':bid,
    })

def bid_winner():
    winner = bidders_data[0]
    for bidder in bidders_data:
        if bidder['bid'] > winner['bid']:
            winner = bidder
    
    print(f"The winner is {winner['name']} with the bid ${winner['bid']}");

while next_player:
    clear()
    name = input("What is your name ? \n")
    bid = float(input("What is your bid ? \n"))
    next_bidder = input("Are there any more bidders ?\ny for yes\nn for no\n").lower()

    add_bidders_data(name,bid)

    if next_bidder =="n":
        next_player=False
        bid_winner()