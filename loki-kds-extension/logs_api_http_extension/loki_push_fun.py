import json
from datetime import datetime
from urllib import request


def push_multi_logs(logs):
    payload = {"streams": [{"stream": {"app": "hello_lambda"}, "values": []}]}
    for one_log in logs:
        time = one_log["time"]
        dt = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
        timestamp = int(dt.timestamp() * 1e9)  # 转化成纳秒
        type = one_log["type"]
        record = str(one_log["record"])
        payload["streams"][0]["values"].append([str(timestamp), f"[{type}] {record}"])

    print(payload)

    loki_url = "http://34.223.23.146:3100/loki/api/v1/push"
    headers = {"Content-type": "application/json", "X-Scope-OrgID": "1"}

    payload = json.dumps(payload).encode("utf-8")
    req = request.Request(loki_url, data=payload, method="POST", headers=headers)
    with request.urlopen(req) as f:
        resp_data = f.read()
        print(resp_data.decode("utf-8"))

        # type = one_log["type"]
        # record = str(one_log["record"])
        # print(f"Now push: [{type}] {record}")
        # push_one_log(time, f"[{type}] {record}")


def push_one_log(time, message):
    loki_url = "http://34.223.23.146:3100/loki/api/v1/push"
    headers = {"Content-type": "application/json", "X-Scope-OrgID": "1"}

    dt = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
    timestamp = int(dt.timestamp())
    # payload = {
    #     "streams": [
    #         {
    #             "labels": '{app="mylambda"}',
    #             "entries": [{"ts": timestamp, "line": message}],
    #         }
    #     ]
    # }
    # payload = {
    #     "streams": [
    #         {
    #             "stream": {"label": "value"},
    #             "values": [
    #                 ["<unix epoch in nanoseconds>", "<log line>"],
    #                 ["<unix epoch in nanoseconds>", "<log line>"],
    #             ],
    #         }
    #     ]
    # }
    payload = json.dumps(payload).encode("utf-8")
    # answer = requests.post(loki_url, data=payload, headers=headers)
    # print(answer)

    req = request.Request(loki_url, data=payload, method="POST", headers=headers)
    with request.urlopen(req) as f:
        resp_data = f.read()
        print(resp_data.decode("utf-8"))


def loki_push(lambda_logs):
    # print(lambda_logs)
    # j_logs = json.loads(lambda_logs)
    for one_log in lambda_logs:
        time = one_log["time"]  # 2024-04-26T04:12:48.974Z
        type = one_log["type"]
        record = str(one_log["record"])
        print(f"Now push: [{type}] {record}")
        push_one_log(time, f"[{type}] {record}")
        # if type == "platform.start":
        #     push_one_log(time, "[platform.start]" + record)
        # if type == "function":
        #     push_one_log(time, "[function]" + record)
