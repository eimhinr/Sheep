import csv
# import pandas as pd

#####################################
#                                   #
#           Answer Class            #
#                                   #
#####################################

class Answers():
    rnd = list(x for x in range(1,27))
    def __init__(self):
        pass

    def print_round_score(self):
        pass


#####################################
#                                   #
#           Playre Class            #
#                                   #
#####################################

class Player():

    def __init__(self, name="", score=0):
            self.name = name
            self.score = score


#####################################
#                                   #
#           IMPORT ANSWERS          #
#                                   #
#####################################

# Read text file
def read_text(file):
    with open("dataset.txt") as f:
        content = f.readlines()
    content = [x.rstrip('\n\t') for x in content]
    return content
    #print(content)

def create_sub_lists(raw):
    answers_dict = {}
    for v in raw:
        if "From:" in v:
            answers_dict[v] = raw[raw.index(v)+2:raw.index(v)+26]
        else:
            pass
            #print("none")
    return answers_dict


def process_answers(file):
    raw_answers = read_text(file)
    data_dict = create_sub_lists(raw_answers)
    for k, v in data_dict.items():
        print("----\n" + "".join(k))
        print("\n".join(v))
        # for val in v:
        #     print("\n".join(val))
    


#####################################
#                                   #
#           CLEAN DATA              #
#                                   #
#####################################
'''

# convert to a DataFrame and render.
# Items to Clean
spec_chars = ["!",'"',"#","%","&","'","(",")",
              "*","+",",","-",".","/",":",";","<",
              "=",">","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–"]

df = pd.DataFrame.from_records(rows)

df = df.rename(columns=df.iloc[0]).drop(df.index[0])  # set the row names
df = df.transpose()                                   # transpose table 
df = df.rename(columns=df.iloc[0]).drop(df.index[0])  #set the column names 
df = df.transpose()
# df = df.columns = df.iloc[1]

# clean data 

# delete speciial chars, replace with space
for row in df:
  for char in spec_chars:
    df[row] = df[row].str.replace(char, ' ') 
                
  # split and rejoin to remove white  spaces
  df[row] = df[row].str.split()\
                .str.join(" ")\
                .str.title() # set all to title case
df.head()
'''

#####################################
#                                   #
#               Main                #
#                                   #
#####################################

def main():
    file = 'dataset.txt'
    process_answers(file)
    pass



#####################################
#                                   #
#               Tests               #
#                                   #
#####################################

def test_class_player():
    print('>>>   Class: Player - Tests started   <<<')
    player = Player()
    player.name = "Eimhin Rafferty"
    print(player.name)
    print('>>>   Class: Player - Tests finished   <<<')

def test_class_answer():
    print('>>>   Class: Answer - Tests started   <<<')
    answer = Answers()
    #answer.rnd = "Eimhin Rafferty"
    print(answer.rnd)
    print('>>>   Class: Answer - Tests finished   <<<')







#####################################
#                                   #
#             Execute               #
#                                   #
#####################################

if __name__ == "__main__":
    main()
    # test_class_player()

    # test_class_answer()