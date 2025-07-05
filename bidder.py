def total_bid(bids):
    high_bid=0
    winner=""
    for biddes in bids:
        bid_amount=bids[biddes]
        if bid_amount>high_bid:
            high_bid=bid_amount
            winner=biddes
    print(f"the winner {winner} with bid amount {high_bid}")


bids={}
bidded_final=False
while not bidded_final:
    bidder_name=input("enter your name:")
    amount=int(input("enter the bid amount:"))
    bids[bidder_name]=amount
    condition=input("if any bid is more give YES or NO:")
    if condition=="no":
        bidded_final=True
        total_bid(bids)
    elif condition=="yes":
        print("enter the next bid")
    else:
        print("enter valid answer")

