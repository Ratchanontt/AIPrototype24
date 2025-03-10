# Web Service
> มีหน้าที่ประมวลผลระหว่างโปรแกรม

> รับมา แล้ว ส่งเครดิตไปให้ปลายทาง

# Web Service for Sending Messages
> เป็น Web Service ที่สามารถส่งข้อความระหว่างผู้ใช้ได้ โดยประกอบไปด้วย 2 ส่วนหลัก:

## 1. **สคริปต์ฝั่งผู้ใช้** [`call_web_service.py`](https://github.com/Ratchanontt/AIPrototype24/blob/main/call_web_service.py): 
> ช่วยให้ผู้ใช้ป้อนข้อความและเลือกผู้รับเพื่อส่งข้อความ
สคริปต์ฝั่งผู้ใช้จะติดต่อกับ API ฝั่งเซิร์ฟเวอร์เพื่อส่งข้อความ โดยมีขั้นตอนดังนี้:
- ผู้ใช้จะป้อนข้อความที่ต้องการส่ง
- ผู้ใช้สามารถเลือกผู้รับได้จาก IP Address
- ส่งข้อความที่เลือกไปยังเซิร์ฟเวอร์ผ่านคำขอ HTTP POST

สคริปต์จะส่งข้อมูลต่อไปนี้ไปยังเซิร์ฟเวอร์:
- `msg`: ข้อความที่ผู้ใช้ป้อน
- `ผู้รับ`: ชื่อของผู้รับข้อความ
- `ip`: ที่อยู่ IP ของผู้รับ
- `ผู้ส่ง`: ชื่อของผู้ส่งข้อความ

**Code**:
```python
import requests
import json

url = 'http://40.81.22.119:5006/simpleAPI'
myobj = {'msg':'Ratchanont'}

x = requests.post(url, data = json.dumps(myobj))
```

## 2. **API ฝั่งเซิร์ฟเวอร์** [`firstflask.py`](https://github.com/Ratchanontt/AIPrototype24/blob/main/firstflask.py): 
> รับข้อความจากผู้ใช้ บันทึกรายละเอียด และส่งคำตอบกลับไปยืนยันการรับข้อความ

**Code**:
```python
  @app.route('/simpleAPI',methods=['POST'])
  def web_service_API():

     payload = request.data.decode("utf-8")
     inmessage = json.loads(payload)

     print(inmessage)
    
     json_data = json.dumps({'y': 'received!'})
     return json_data
```
