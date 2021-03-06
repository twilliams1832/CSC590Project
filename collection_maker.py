import json

genres = {'0' : 'swing',
              '1' : 'ballad',
              '2' : 'funkRock',
              '3' : 'latin',
              '4' : 'bebop'}

def checkNumber(option):
    if len(option) > 1 or (not option.isdigit()) or int(option) > 20 or int(option) < 1:
        return False
    return True


def numberOfFields():
    while 1:
        numFields = input("How many fields?")
        if(checkNumber(numFields)):
            return int(numFields)
        else:
            print("Invalid number of fields")

def setFields(numFields):
    fields = []
    for i in range(numFields):
        input_string = "Field " + str(i+1) + " name:"
        field = input(input_string)
        fields.append(field)

    return fields

def isFieldGenre():
    while 1:
        choice = input("Is one of the fields genre?(Y/N)")
        if(choice.lower() == 'y'):
            return True
        elif(choice.lower() == 'n'):
            return False
        else:
            print("Invalid choice")
            
def createCollection():
    f = open('collection_out', 'w')
    collection = []
    i = 0
    
    numFields = numberOfFields()
    fields = setFields(numFields)
    genreField = isFieldGenre()
    goAhead = True
    
    while goAhead:
        fieldMember = {}
        for field in fields:
            input_string = field+": "
            current_field = input(input_string)
            if current_field == "quit":
                goAhead = False
                break
            
            fieldMember[field] = current_field
        if goAhead:
            if genreField:
                fieldMember['genre'] = genres[input('genre:')]
                collection.append(fieldMember)
        
            print(collection[i])
            i += 1

    json_string = ''

    for item in collection:
        for field in fields:
            json_string += '{"' + field + '":"' + item[field] + '"},\n'
            
    f.write(json_string)

def checkInput(option):
    if len(option) > 1 or (not option.isdigit()) or int(option) > 3 or int(option) < 1:
        return False
    return True

def editCollection():
    fileName = input("filename:")
    f = open(fileName, "r")
    out = open("piecelistview.txt", "w+") 
    jsonFile = f.read()
    collection = eval(jsonFile)

    i = 1
    out_string = ""
    
    print("Collection")
    for item in collection['collection']:
        out_string += item['view']
        print(str(i)+". "+item['title'])
        print("    "+item['artist'])
        print("    "+item['genre'])
        print("    "+item['view'])
        print("    "+item['videoURL'])
        i += 1
        out_string += "\n"

    out.write(out_string)
    
    
    
    
def menu():
    print("JSON Collection Maker")
    print("1. Create new collection")
    print("2. Edit existing collection")
    print("3. Exit")
    
    while True:
        option = input(">>>")
        if(checkInput(option) == False):
            print("Invalid input")
        else:
           if option == "1":
               createCollection()
           elif option == "2":
               editCollection()
           else:
               break
    
menu()
