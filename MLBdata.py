def main():
    myFile = open("MLB_Pitching.csv", 'r')

    team_data = []

    for line in myFile:
        info = line.split(",")
        teamName = info[0]
        runsAllowed = info[3]
        wins = info[4]
        losses = info[5]
        era = info[7]

        team_data.append([teamName, "", runsAllowed, wins, losses, era])
        

    myFile.close()

    hittingFile = open("MLB_Hitting.csv", 'r')

    teamCount = 0

    for line in hittingFile:
       info = line.split(",")
       runsScored = info[3]
       team_data[teamCount][1] = runsScored
       print(team_data[teamCount])
       teamCount = teamCount + 1
       

    hittingFile.close()

    outFile = open("mlb_output.csv", 'w')

    for line in team_data:
       #[teamName, "runsscored", runsAllowed, wins, losses, era])
       output = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + line[5] + "\n"
       
       outFile.write(output)

    outFile.close()

if __name__ == '__main__':
  main()