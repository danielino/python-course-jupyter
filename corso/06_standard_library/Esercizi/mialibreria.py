import json

# rubrica telefonica


def stacca_id(items):
    if len(items) == 0:
        return 0
    return items[-1]['id'] + 1

def creazione_record(rubrica, nome, cognome, numero, email = None):
    """
    param: nome       nome del contatto
    param: cognome    cognome del contatto
    param: numero     numero del contatto
    """
    item = {
        "id" : stacca_id(rubrica),
        "nome" : nome,
        "cognome" : cognome,
        "numero" : numero,
        "email" : email
    }
    rubrica.append(item)
    return item

def cerca_record(rubrica, nome = "", cognome = "" , numero = "" ):
    # iterazione della lista database
    for item in rubrica:
        if item['nome'].upper() == nome.upper() and item['cognome'].upper() == cognome.upper():
            return item
        elif item['numero'] == numero:
            return item
        
    return False


def elimina_record(item_id, rubrica):
    for item in rubrica:
        if item_id == item['id']:
            rubrica.remove(item)

            
def write_file(fileName, content):
    fp = open(fileName, 'a+')
    fp.write(content)
    fp.close()
          
def main():
    rub = []

    creazione_record(rub, "marco", "rossi" ,"192911")
    creazione_record(rub, "pietro", "bianchi" ,"19291212991")
       
    print(json.dumps(rub))
    
if __name__ == "__main__":
    main()
    
 