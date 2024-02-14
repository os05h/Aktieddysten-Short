from API import Aktiedysten_API
import json

#Open private json
private = json.load(open('private.json'))
account = Aktiedysten_API(private['Username'], private['Password'], private['Game'])