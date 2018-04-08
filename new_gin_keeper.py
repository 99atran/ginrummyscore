print "Welcome to the Gin Rummy Scorekeeper."
print

Player_1_name = raw_input("Player 1 Name: ")
Player_2_name = raw_input("Player 2 Name: ")

print
print "Here are my scoring rules:"
print "10-Card Gin Bonus is +25."
print "11-Card Big Gin Bonus is +31."
print "If there is no round winner, no points are awarded including Gin and Big Gin bonuses."
print "No Undercut bonus."
print "Line Bonus is +25 per hand won."
print "Game Bonus is +100 for winner."
print "Shoutout Bonus doubles total score before Line and Game bonuses to winner."
print
print "For pre-scoring and set-matching rules, check out the Gin Rummy page on Wikipedia."
print

score_max = int(input("What score are you playing to? "))

score_1 = 0
score_2 = 0

wins1 = 0
wins2 = 0

print Player_1_name, "Score:", score_1
print Player_2_name,"Score:", score_2

round_number = 0

def round_up():
    global round_number
    round_number += 1

def scoring():

    global score_1
    global score_2
    global wins1
    global wins2
    round_score1 = 0
    round_score2 = 0

    print Player_1_name, ":"
    ace1 = int(input("# of Aces: "))
    two1 = int(input("# of 2s: "))
    three1 = int(input("# of 3s: "))
    four1 = int(input("# of 4s: "))
    five1 = int(input("# of 5s: "))
    six1 = int(input("# of 6s: "))
    seven1 = int(input("# of 7s: "))
    eight1 = int(input("# of 8s: "))
    nine1 = int(input("# of 9s: "))
    ten1 = int(input("# of 10s: "))
    jack1 = int(input("# of Jacks: "))
    queen1 = int(input("# of Queens: "))
    king1 = int(input("# of Kings: "))

    if ace1+two1+three1+four1+five1+six1+seven1+eight1+nine1+ten1+jack1+queen1+king1 == 0:
        print
        ginny1 = int(input("10 or 11 cards? "))
        if ginny1 == 10:
            score_1 += 25
            print "Gin! Bonus points awarded to total score."
        elif ginny1 == 11:
            score_1 += 31
            print "Big Gin! Bonus points awarded to total score."
    print

    round_score1 = ace1 + two1 * 2 + three1 * 3 + four1 * 4 + five1 * 5 + six1 * 6 + seven1 * 7 + eight1 * 8 + nine1 * 9 + (ten1 + jack1 + queen1 + king1) * 10
    print Player_1_name, round_score1

    print
    print Player_2_name, ":"
    ace2 = int(input("# of Aces: "))
    two2 = int(input("# of 2s: "))
    three2 = int(input("# of 3s: "))
    four2 = int(input("# of 4s: "))
    five2 = int(input("# of 5s: "))
    six2 = int(input("# of 6s: "))
    seven2 = int(input("# of 7s: "))
    eight2 = int(input("# of 8s: "))
    nine2 = int(input("# of 9s: "))
    ten2 = int(input("# of 10s: "))
    jack2 = int(input("# of Jacks: "))
    queen2 = int(input("# of Queens: "))
    king2 = int(input("# of Kings: "))

    if  ace2+two2+three2+four2+five2+six2+seven2+eight2+nine2+ten2+jack2+queen2+king2 == 0:
        print
        ginny2 = int(input("10 or 11 cards? "))
        if ginny2 == 10:
            score_2 += 25
            print "Gin! Bonus points awarded to total score."
        elif ginny2 == 11:
            score_2 += 31
            print "Big Gin! Bonus points awarded to total."

    print
    round_score2 = ace2 + two2 * 2 + three2 * 3 + four2 * 4 + five2 * 5 + six2 * 6 + seven2 * 7 + eight2 * 8 + nine2 * 9 + (ten2 + jack2 + queen2 + king2) * 10
    print Player_2_name, round_score2
    print
    if round_score1 > round_score2:
        net_round = round_score1 - round_score2
        score_2 += net_round
        wins2 += 1
        print Player_2_name, "wins", net_round, "points!"
    elif round_score2 > round_score1:
        net_round = round_score2 - round_score1
        score_1 += net_round
        wins1 += 1
        print Player_1_name, "wins", net_round, "points!"
    elif round_score1 == round_score2:
        print "tie!"
        ginY1 = raw_input("Did " + str(Player_1_name) + " have Gin? (yes or no) " )
        if ginY1 == "yes":
            score_1 -= 25
        else:
            bigY1 = raw_input("Did " + str(Player_1_name) + " have Big Gin? (yes or no) " )
            if bigY1 == "yes":
                score_1 -= 31

        ginY2 = raw_input("Did " + str(Player_2_name) + " have Gin? (yes or no) " )
        if ginY2 == "yes":
            score_2 -= 25
        else:
            bigY2 = raw_input("Did " + str(Player_2_name) + " have Big Gin? (yes or no) " )
            if bigY2 == "yes":
                score_2 -= 31
                

while 0 <= score_1 <= score_max and 0 <= score_2 <= score_max or score_1 == score_2:
    round_up()
    print
    print "Round", round_number
    print
    scoring()
    print
    print "Current Scores:"
    print Player_1_name, score_1
    print Player_2_name, score_2
    print

if score_1 >= score_max and score_1 > score_2:
    if wins2 == 0:
        score_1 += score_1
    score_1 += (wins1 * 25)    
    score_1 += 100
    print Player_1_name, "has won the game", score_1, "to", score_2
elif score_2 >= score_max and score_2 > score_1:
    if wins2 ==0:
        score_2 += score_2
    score_2 += (wins2 * 25)
    score_2 += 100
    print Player_2_name, "has won the game", score_2, "to", score_1
