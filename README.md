# have-my-contacts-been-pwned-in-facebook533m-leak
This python script quickly tells you which of your contacts have been affected by the 533m Facebook leak. You need your contacts (they are yours) and the leak (it is public). The information input is in csv format with the following fields.

Your csv contacts file: {'Name': 'string', 'Phone': 'string'}

The csv leaks file:  {'phone': 'string', 'profile-id': 'string', 'name': 'string', 'family-name': 'string', 'genre': 'string',
                                        'location-now': 'string', 'location-birth': 'string', 'single-status': 'string', 'employment': 'string',
                                        'graduation-date': 'string', 'email': 'string', 'birth-date': 'string'}

The output is a csv file with format (includes the Name from our csv contacts file with the affected row from the csv leaks file):
{'phone': 'string', 'profile-id': 'string', 'name': 'string', 'family-name': 'string', 'genre': 'string',
                                        'location-now': 'string', 'location-birth': 'string', 'single-status': 'string', 'employment': 'string',
                                        'graduation-date': 'string', 'email': 'string', 'birth-date': 'string', 'Name': 'string'}

The csv uses the phone format:international_code number (without any separator between fiels or numbers: 349000000, like in the csv leak file)
