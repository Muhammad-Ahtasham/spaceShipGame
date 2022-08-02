    if redHealth <=0:
                winnerText = "yellow Wins"
            if yellowHealth <=0:
                winnerText = "Red Wins"
            if winnerText != "":
                drawWinner(winnerText)
                break