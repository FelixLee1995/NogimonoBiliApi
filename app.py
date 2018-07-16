from flask import Flask
import service
import json

app = Flask(__name__)


@app.route('/dynamic/get/<index>/<size>')
def getDynamicByPagination(index, size):
    res = service.getPaginationDynamic(int(index), int(size))
    if res == -1:
        resp = {'code': 200, 'status': 0, 'msg': '获取动态失败'}
    else:
        if (int(index) + 1)*int(size) < service.getDynamicTotalCount():
            resp = {'code': 200, 'status': 1, 'msg': '获取动态成功', 'hasmore': 1, 'data': res}
        else:
            resp = {'code': 200, 'status': 1, 'msg': '获取动态成功', 'hasmore': 0, 'data': res}
    return json.dumps(resp, ensure_ascii=False)


if __name__ == '__main__':
    app.run(port=5001)
