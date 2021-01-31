import pandas as pd
import json
import logging
# from TN import TN

# network = TN()
log = logging.getLogger()
log.info("File is being called process_cvs")

def test():
    return True

def processFile(db):
    log.info("process file")
    df = pd.read_csv("/code/db/data1.csv")
    print(df.head(10))
    log.info("process read complete")
    # print(df.head(10))
    #dates, df = df['CPT/HCPCS & Description'], df.iloc[:, 1:]
    date_order = ('code', 'description')
    #print(df['CPT/HCPCS & Description'])
    for i,col in enumerate( date_order):
        #print(i, col)
        df[col]=df['CPT/HCPCS & Description'].map( lambda x: x.split(' - ')[i].strip() if type(x) == str else 'AAAAA' )
        #df[col] = df['CPT/HCPCS & Description'].map( lambda x: x.split(' - ')[i].strip() )

    groupby = df.sort_values(["Patient Account Number","Date Of Service"], ascending=True)
    billing_codes = []
    patient_acct_number = ''
    count = 0
    listcount= []
    for index, row in groupby.iterrows():

        #og.info(row)

        if patient_acct_number == '' or row[0] == patient_acct_number:
            if row[4] not in billing_codes:
                billing_codes.append(row[4])
        else:
            #print("Sending to N-ary Tree ", billing_codes)
            #print(billing_codes)
            # Only uncomment if we want patient and medical records
            if ['20650','27252','27268','99223'] == billing_codes:
                count += 1
                listcount.append(row[0])
            db.insert_record(row[0], row[1], billing_codes)
            # network.insert(billing_codes)
            billing_codes = [row[4]]

        # if index == 2000:
        #     break
        patient_acct_number = row[0]
    log.info("Number occur : " + str(count))
    log.info("List number : " + str(listcount))
    return True
# processFile("AA")
#print ("Done")

#print(groupby.head(25))

#True if x % 2 == 0 else False



# a = TN()
# a.insert(["20650", "27252", "27268", "99223"])
#print("***********************")
# a.progress_insert_nodes([20650, 27252, 27268, 99223])
# print("**************")
# a.progress_insert_nodes([20650, 27252, 99223, 27268])
# print("**************")
# a.progress_insert_nodes([20650, 27268, 27252, 99223])
# print("************** error")
# a.progress_insert_nodes([20650, 27268, 99223, 27252])
#a.progress_insert_nodes([20650, 99223, 27252, 27268])
# a.progress_insert_nodes([20650, 99223, 27268, 27252])
# a.insert([20650, 27268, 27252, 99223])
# a.insert([20650, 27268, 99223, 27252])
# import os
# def import_input():
#     print("Total network is : ", len(network.P_Node), network.P_Node)
#     answer = ""
#     while answer != "y":
#         answer = input("Enter your billing code : ")
#         os.system('cls' if os.name == 'nt' else 'clear')
#         root = network.search_parent_node(answer, searchable=True)
#         if root:
#         #a.verified(root)
#             network.traverse(root)
#             network.reset_mapsubset()
#         else:
#             print("This bill code ( ", answer, " ) not found !!!")