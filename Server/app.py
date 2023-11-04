from flask import Flask, jsonify, request
from flask_cors import CORS
from copy import copy
import os
from dotenv import load_dotenv
from SystemManagement import cpuInfo, memoryInfo
from StorageDeviceManagement import diskInfo
from UserManagement import crudUser
from StorageManagement import readDirectory

app = Flask(__name__)
CORS(app)

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

global userInfo, templOrig
userInfo = None
templOrig = {
    "status": None,
    "msg": None,
    "data": None
}


@app.route('/', methods=["GET"])
def check_server():
    global userInfo, templOrig
    templ = copy(templOrig)
    templ['status'] = 200
    templ['msg'] = "Service operating normally."
    templ['data'] = {"current_user": userInfo}
    return jsonify(templ)


# [ 사용자 CRUD ]


@app.route('/user/create', methods=["POST"])  # [ 사용자 생성 ]
def user_create():
    data = request.get_json()
    response = crudUser.create_user(
        id=data["id"], pw=data["pw"], desc=data["desc"])
    return jsonify(response)


@app.route('/user/list', methods=["GET"])  # [ 사용자 목록 조회 ]
def user_list():
    key = request.args.get('key', "")
    response = crudUser.get_user_list(key)
    return jsonify(response)


@app.route('/user/info', methods=["GET"])  # [ 사용자 정보 조회 ]
def user_info():
    key = request.args.get('key', "")
    id = request.args.get('id', "")
    response = crudUser.get_user_info(key, id)
    return jsonify(response)


@app.route('/user/update', methods=["POST"])  # [ 사용자 정보 수정 ]
def user_update():
    data = request.get_json()
    response = crudUser.update_user(
        id=data["id"], pw=data["pw"], desc=data["desc"])
    return jsonify(response)


@app.route('/user/delete', methods=["GET"])  # [ 사용자 삭제 ]
def user_delete():
    key = request.args.get('key', "")
    id = request.args.get('id', "")
    response = crudUser.delete_user(
        key=key, id=id)
    return jsonify(response)


@app.route('/sign/in', methods=["POST"])
def sign_in():
    data = request.get_json()
    key = "password"
    response = crudUser.get_user_info(key, data["id"])
    if response != None and response["pw"] == data["pw"]:
        return jsonify(response)
    else:
        return jsonify(None)


@app.route('/sign/up', methods=["POST"])
def sign_up():
    data = request.get_json()
    print(data)
    response = crudUser.create_user(
        id=data["id"], pw=data["pw"], desc=data["id"] + " Account.")
    print(response)
    if type(response) == dict:
        return jsonify(response)
    else:
        return jsonify(None)


@app.route('/system/cpu', methods=["GET"])  # [ 시스템(CPU) 상태 조회 ]
def view_cpu():
    response = cpuInfo.main(False)
    return jsonify(response)


@app.route('/system/memory', methods=["GET"])  # [ 시스템(MEMORY) 상태 조회 ]
def view_memory():
    response = memoryInfo.main(False)
    return jsonify(response)


@app.route('/system/disk', methods=["GET"])  # [ 시스템(DISK) 상태 조회 ]
def view_disk():
    response = diskInfo.main(False)
    return jsonify(response)


@app.route('/storage/read', methods=["POST"])  # [ 시스템(DISK) 상태 조회 ]
def view_directory():
    data = request.get_json()
    response = readDirectory.get_directory_list(data['path'])
    return jsonify(response)


@app.route('/summary', methods=["POST"])
def get_summary():
    print("summary 화면 데이터 전송")


@app.route('/storage', methods=["POST"])
def get_storage():
    print("storage 화면 데이터 전송")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
