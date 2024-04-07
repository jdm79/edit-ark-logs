import pprint

shoot_log = "ShooterGame.log"
snippet = "text.txt"

# import the text file
ark_log = open(snippet, 'r')

# split the list at each exclamation mark 
arked = [line.split('!') for line in ark_log.readlines()]
# use a for loop to get rid of the first timestamp in each item in list

# for loop to clean up each line
with open("result.txt", "w") as output:
  for line in arked:
    # remove the duplicate timestamp from each log item
    n = 30
    line = line[0][n:]

    # remove the first 3 characters from the string, but nothing from the end
    line = str(line) [3:]

    # bad_words = ["Saving world", "Garbage Collection Triggered", "World Save Complete"]
    str1 = "Saving world..."
    str2 = "Collection Triggered"
    str3 = "World Save Complete"
    # remove empty strings and any including the strings above
    if len(line) > 0 and not str1 in line and not str2 in line and not str3 in line:    
      output.write(str(line) + "\n")