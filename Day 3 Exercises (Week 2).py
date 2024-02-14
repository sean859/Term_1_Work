# List
def List():
    Shopping_List = []
    print(Shopping_List)
    Shopping_List = ["Apple", "Banana", "Orange"]
    print(Shopping_List)
    Shopping_List = ["Apple", "Grapes", "Orange"]
    print(Shopping_List)
List()

# Tuple
def Tuple():
    Coordinates = (156, 178)
    print(Coordinates)
    Updated_Coordinates = (194, 178)
    print(Updated_Coordinates)

    Fruit = ("Apple", "Dragonfruit", "Apriocot")
    print(Fruit[1])
    print(Fruit.count("Banana"))
Tuple()

# Dictionary
def Dictionary():
    Library ={'Lord Of The Flies': 'William Golding', 'The Book Thief': 'Markus Zusak', 'Iron Flame': 'Rebecca Yarros'}
    print(Library)
    def create_dictionary():
        randomwords =['Hello', 'Dragonfruit', 'Backup', 'Calling']
        randomwords_dictionary ={randomwords[0]: 5, randomwords[1]: 11, randomwords[2]: 6, randomwords[3]: 7}
        print(randomwords_dictionary)
    create_dictionary()
Dictionary()

# Set
def Set():
    def Two_List_Common():
        list_1 =[1, 2, 3, 4, 5]
        list_2 =[1, 3, 5, 6, 7]
        list_common = list(set(list_1).intersection(list_2))
        print(list_common)
    Two_List_Common()
    
    list_1 =[1, 2, 3, 4, 5]
    list_2 =[1, 3, 5, 6, 7]
    list_joined = list(set(list_1 + list_2))
    print(list_joined)
Set()
