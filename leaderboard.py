# Stylianos Dimitriadis
import os.path


class Leaderboard():
    
    def __init__(self):
        self.filename = "leaderboard.txt"

    #either creates file or returns top 5(or less) if already exists
    def build(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                lines = [line.rstrip() for line in file]
                if len(lines) < 5:
                    return lines
                else:
                    return lines[:5]
        else:
            with open(self.filename, "w+") as file:
                return None
        
    
    def update(self, username, score):
        stringline = f"{username}, {score}\n"
        #Open file in reading/writing mode
        with open(self.filename, "r+") as lfile:
            #Read file into lines
            lines = lfile.readlines()
            if len(lines) > 0:
                for index, line in enumerate(lines):
                    if line != "":
                        #Split line into username, score
                        line_score = int(line.split(", ")[1])
                        #Compare scores (inserts or adds to end if it gets to end of list)
                        if line_score < score or index == len(lines) - 1:
                            lines.insert(index, stringline)
                            break
            else:
                #Append if it's the first entry
                lines.append(stringline)
        
            #Write whole list of lines back to file - Overwrite
            lfile.seek(0)
            for line in lines:
                lfile.write(line)
            lfile.truncate()
    
#<user>, <score>
#l1 = Leaderboard()
#l1.build()
#print(l1.build())
#l1.update("Steve", 1)
#l1.update("Ayman", 3)
#l1.update("Thomas", 2)
#print(l1.build())