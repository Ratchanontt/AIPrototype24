import requests
import json
import sqlite3

# ----------------------------------------------------- #
### Prototype Code ###
# url = 'http://40.81.22.119:5006/simpleAPI'
# myobj = {'msg':'Ratchanont'}

# x = requests.post(url, data = json.dumps(myobj))
# ----------------------------------------------------- #

# สร้างหรือเชื่อมต่อกับฐานข้อมูล SQLite
# เพื่อเพิ่มเพื่อนและส่งข้อความหาคนที่ไม่มีในรายชื่อ
conn = sqlite3.connect('message_records.db')
cur = conn.cursor()

# สร้างตารางถ้ายังไม่มี
cur.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT,
    recipient TEXT,
    recipient_ip TEXT,
    message TEXT,
    status_code INTEGER,
    response_text TEXT
)
''')
conn.commit()

# URL ของ API
url = 'http://40.81.22.119:5006/simpleAPI'

# ป้อนข้อความจากผู้ใช้
msg = input("ป้อนข้อความที่คุณต้องการส่ง: ")

# เลือกคนที่ต้องการส่งข้อความ
print("\nคุณต้องการส่งข้อความหาใคร?:")
print("1. Guitar (IP: 104.43.58.161)")
print("2. Ploy (IP: 13.75.95.136)")
print("3. Nont (IP: 40.81.22.119)")
print("4. Moo (IP: 57.155.113.7)")
print("5. ระบุผู้รับใหม่")

choice = input("กรุณาระบุคนที่ต้องการส่ง: ")

# กำหนด IP และชื่อผู้รับตามตัวเลือก
if choice == '1':
    recipient = "Guitar"
    ip = "104.43.58.161"
elif choice == '2':
    recipient = "Ploy"
    ip = "13.75.95.136"
elif choice == '3':
    recipient = "Nont"
    ip = "40.81.22.119"
elif choice == '4':
    recipient = "Moo"
    ip = "57.155.113.7"
elif choice == '0':
    recipient = input("กรุณาป้อนชื่อผู้รับใหม่: ")
    ip = input("กรุณาป้อน IP Address ของผู้รับใหม่: ")
else:
    print("\n[ERROR] ตัวเลือกไม่ถูกต้อง! กรุณาเลือกตัวเลือกที่ถูกต้อง.")
    exit()

# ชื่อผู้ส่ง
sender = "nnnt" # ชื่อของเรา

# สร้าง dictionary สำหรับข้อมูลที่จะส่งไป
myobj = {
    'message_key': 'message_val',
    'msg': msg,  # ใช้ข้อความที่ผู้ใช้ป้อน
    'ผู้รับ': recipient,  # ชื่อผู้รับ
    'ip': ip,  # IP ของผู้รับ
    'ผู้ส่ง': sender  # ชื่อผู้ส่ง
}

# แสดงข้อมูลก่อนส่ง
print("\nกำลังส่งข้อความ... \n")
print(f"ข้อมูลที่ส่งไป: ")
print(f"----------------------------")
print(f"ผู้ส่ง: {sender}")
print(f"ผู้รับ: {recipient}")
print(f"IP ของผู้รับ: {ip}")
print(f"ข้อความที่ส่ง: {msg}")
print(f"----------------------------\n")

# ส่งคำขอ POST
try:
    response = requests.post(url, data=json.dumps(myobj), timeout=90)
    response.raise_for_status()
    print(f"การส่งข้อความสำเร็จ! คำตอบจาก API: {response.text}")
    status_code = response.status_code
    response_text = response.text
except requests.exceptions.HTTPError as errh:
    print("ข้อผิดพลาด HTTP:", errh)
    status_code = response.status_code if response else None
    response_text = str(errh)
except requests.exceptions.ConnectionError as errc:
    print("ข้อผิดพลาดการเชื่อมต่อ:", errc)
    status_code = None
    response_text = str(errc)
except requests.exceptions.Timeout as errt:
    print("ข้อผิดพลาด Timeout:", errt)
    status_code = None
    response_text = str(errt)
except requests.exceptions.RequestException as err:
    print("Oops: เกิดข้อผิดพลาดบางอย่าง", err)
    status_code = None
    response_text = str(err)

# บันทึกข้อมูลในฐานข้อมูล
cur.execute('''
INSERT INTO messages (sender, recipient, recipient_ip, message, status_code, response_text)
VALUES (?, ?, ?, ?, ?, ?)
''', (sender, recipient, ip, msg, status_code, response_text))
conn.commit()

# ปิดการเชื่อมต่อกับฐานข้อมูล
conn.close()