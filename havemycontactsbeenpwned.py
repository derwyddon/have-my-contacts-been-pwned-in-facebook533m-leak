from argparse import ArgumentParser

import time  # timer

import pandas as pd

if __name__ == '__main__':
    ap = ArgumentParser()

    ap.add_argument("-c", "--contacts", type=str, required=True, help="contacts input csv file")
    ap.add_argument("-dl", "--data_leak", type=str, required=True, help="data leak input csv file")

    args = vars(ap.parse_args())

    contacts_file = args["contacts"]
    dataleak_file = args["data_leak"]


    t_start = time.perf_counter()

    leak = list()
    phones = list()

    leak = pd.read_csv(dataleak_file, header = 0, sep = ':', decimal = ',', encoding = 'utf-8', keep_default_na = False, verbose=True, dtype =
                                       {'phone': 'string', 'profile-id': 'string', 'name': 'string', 'family-name': 'string', 'genre': 'string',
                                        'location-now': 'string', 'location-birth': 'string', 'single': 'string', 'employment': 'string',
                                        'quinta': 'string', 'email': 'string', 'birth': 'string'}) #Dataframes list

    phones= pd.read_csv(contacts_file, header = 0, sep = ';', decimal = ',', encoding = 'utf-8', keep_default_na = False, dtype =
                                       {'Name': 'string', 'Phone': 'string'}) #Dataframes list

    print("Leak Shape:"+str(leak.shape))
    print("Contacts Shape:"+str(phones.shape))
    df_filt = leak[leak['phone'].isin(phones['Phone'])]


    df_filt_full = pd.merge(df_filt, phones, how="left", left_on=['phone'], right_on=['Phone'], suffixes=('', '_y'))
    df_filt_full.pop('Phone')

    print(df_filt_full)
    t_end_searching_phones = time.perf_counter()
    print("Contacts Filtered Shape:"+str(df_filt_full.shape))
    try:
        my_leaked_contacts_phone_csv = contacts_file + '.fitered.csv'
        df_filt_full.to_csv(my_leaked_contacts_phone_csv, index=False, encoding='utf-8-sig', sep=';')

    except Exception as e:  # we verify the creation of restult files and folders inside reviewed output folder
        print("PROBLEM CREATING or WRITING RESULT LEAKED filtered contacts file " + my_leaked_contacts_phone_csv)
        pass

    print("Searched Phones in Dataset in " +
          str(round(t_end_searching_phones - t_start , 2)) + " seconds "
          )
