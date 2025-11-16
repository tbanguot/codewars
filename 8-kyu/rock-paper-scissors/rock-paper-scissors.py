def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    
    if p1 == "paper":
        return "Player 1 won!" if p2 == "rock" else "Player 2 won!"
    if p1 == "scissors":
        return "Player 1 won!" if p2 == "paper" else "Player 2 won!"
    
    return "Player 1 won!" if p2 == "scissors" else "Player 2 won!"