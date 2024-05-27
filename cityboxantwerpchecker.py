import requests,argparse
import json
from send_email import send
parser = argparse.ArgumentParser()
parser.add_argument("sender",help="Sender Email",type=str)
parser.add_argument("reciver", help="Reciver Email",type=str)
parser.add_argument("password",help="Sender Password",type=str)
parser.add_argument("from_date",help="Data from")
parser.add_argument("to_date",help="Data to")

args = parser.parse_args()

sender_email = args.sender 
receiver_email = str(args.reciver) 
password = str(args.password) 


f = open("data.json")
data = json.load(f)
data["from_date"] =args.from_date
data["to_date"] = args.to_date

headers = {"Content-Type": "text/plain;charset=UTF-8","Accept":"*/*"}
response = requests.post("https://cityboxhotels.com/api/operations/find_available_price",headers=headers,json=data)
msg = []
if (response.json()):
    for i in response.json():
        print("ID: " , i["product_id"])
        print("Suite: " + i["product_name"])
        print("Available: " , i["available"])
        msg.append("ID: {} Suite: {} Available: {} ".format(i["product_id"],i["product_name"],i["available"]))


else:
    print("brak")

if msg:
    send(sender_email, receiver_email, password, msg)