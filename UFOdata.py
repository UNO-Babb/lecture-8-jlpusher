def main():
    myFile = open("ufo_sightings.csv", 'r')

#can you print all the data?
#can you isolate one state?
#can you find the sum total of cases by place?
#Are there any data anomalies you would need to consider?

    for line in myFile:
        info = line.split(",")
        state = info[1]
        city = info[0]
        print(state)
        #info = line.split(",")

    myFile.close()
    
if __name__ == '__main__':
    main()
