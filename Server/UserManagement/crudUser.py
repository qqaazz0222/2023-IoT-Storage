import os
import csv
global PATH_USER_DATA
PATH_USER_DATA = os.getenv("PATH_USER_DATA")
KEY = "password"


def create_user(id=None, pw=None, desc=None):
    if id != None and pw != None and desc != None:
        user_id_list = get_user_id_list()
        if id in user_id_list:
            return "[Error] already used id."
        else:
            f = open(PATH_USER_DATA, 'a')
            wr = csv.writer(f)
            wr.writerow([id, pw, desc])
            return {id: id, pw: pw, desc: desc}
    else:
        return "[Error] not enough parameter."


def get_user_list(key=None):
    if key == KEY:
        f = open(PATH_USER_DATA, 'r')
        d = list(csv.reader(f))
        user_list = []
        table_header = []
        for idx in range(len(d)):
            if idx == 0:
                table_header = d[idx]
            else:
                temp = {}
                for h_idx in range(len(table_header)):
                    temp[table_header[h_idx]] = d[idx][h_idx]
                user_list.append(temp)
        return(user_list)
    else:
        print("[Error] invalid key.")
        return "[Error] invalid key."


def get_user_id_list():
    f = open(PATH_USER_DATA, 'r')
    d = list(csv.reader(f))
    user_id_list = []
    for idx in range(len(d)):
        if idx != 0:
            user_id_list.append(d[idx][0])
    return user_id_list


def get_user_info(key=None, id=None):
    if key == KEY:
        f = open(PATH_USER_DATA, 'r')
        d = list(csv.reader(f))
        user_list = []
        table_header = []
        for idx in range(len(d)):
            if idx == 0:
                table_header = d[idx]
            else:
                if d[idx][0] == id:
                    temp = {}
                    for h_idx in range(len(table_header)):
                        temp[table_header[h_idx]] = d[idx][h_idx]
                    return(temp)
        print("[Error] account does not exist.")
    else:
        return "[Error] invalid key."


def update_user(key=None, id=None, pw=None, desc=None):
    if key == KEY:
        if id != None and pw != None and desc != None:
            user_id_list = get_user_id_list()
            if id in user_id_list:
                fr = open(PATH_USER_DATA, 'r')
                d = list(csv.reader(fr))
                fr.close()
                fw = open(PATH_USER_DATA, 'w')
                wr = csv.writer(fw)
                for l in d:
                    if l[0] != id:
                        wr.writerow(l)
                    else:
                        wr.writerow([id, pw, desc])
                fw.close()
                return {id: id, pw: pw, desc: desc}
            else:
                return "[Error] account does not exist."
        else:
            return "[Error] not enough parameter."
    else:
        return "[Error] invalid key."


def delete_user(key=None, id=None):
    if key == KEY:
        if id != None:
            user_id_list = get_user_id_list()
            if id in user_id_list:
                fr = open(PATH_USER_DATA, 'r')
                d = list(csv.reader(fr))
                fr.close()
                fw = open(PATH_USER_DATA, 'w')
                wr = csv.writer(fw)
                for l in d:
                    if l[0] != id:
                        wr.writerow(l)
                fw.close()
                return f"[Done] {id} account deleted."
            else:
                return "[Error] account does not exist."
        else:
            return "[Error] not enough parameter."
    else:
        return "[Error] invalid key."
