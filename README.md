# have-my-contacts-been-pwned-in-facebook533m-leak
This python script quickly tells you which of your contacts have been affected by the 533m Facebook leak. You need your contacts (they are yours) and the leak (it is public).

Your csv contacts file: {'Name': 'string', 'Phone': 'string'}

The csv leaks file:  {'phone': 'string', 'profile-id': 'string', 'name': 'string', 'family-name': 'string', 'genre': 'string',
                                        'location-now': 'string', 'location-birth': 'string', 'single-status': 'string', 'employment': 'string',
                                        'graduation-date': 'string', 'email': 'string', 'birth-date': 'string'}

phone format:international_code number (without separator between both fiels: 349000000, like in the csv leak file)
