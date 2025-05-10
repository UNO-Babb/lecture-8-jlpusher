def main():
  myFile = open("qbdata.txt", 'r')

  for line in myFile: #my code matches yours from the lecture video but for some reason info is showing as only one spot instead of each item being its own.
    info = line.split(",") 
    td = info[12]
    name = info[0]
    rating = info[1]
    print (name, "had a rating of", rating, "and threw", td, "touchdowns.") 
    

  myFile.close()


if __name__ == '__main__':
  main()
