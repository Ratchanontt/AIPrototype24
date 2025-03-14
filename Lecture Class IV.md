# Web Page
## การสร้างเว็บ มี 3 แบบ
- 1. **Web page** no function, only for looking information
  > เป็น web ที่เราเอาข้อมูลของเราใส่เข้าไป เพื่อให้คนอื่นเข้ามาดูข้อมูลของเรา  
- 2. **Web application** add server side project
  > ** Server side script** (ใช้ในการคิดคำนวณผลลัพทธ์)  
     >> Server side script เช่น Python (Flask package) : ทำให้ user run บน com ที่ไม่ต้องแรงมากได้เพราะมัน run บน  server และทำให้ code ของ dev ไม่หลุดไปไหน
- 3. **Web service** Server side script only
  > ใช้แค่ Server side script Python (Flask package)  เพราะไม่ได้ต้องการให้คนมาใช้
  > เป็น Back end ล้วนๆ ไม่มี front end

## HTTP Methods
### GET คนเห็นแล้วเปิดได้เลย
> GET Method:
- ใช้สำหรับการดึงข้อมูลจากเซิร์ฟเวอร์
- วิธีการนี้ไม่เปลี่ยนแปลงสถานะของเซิร์ฟเวอร์
- ข้อมูลที่ถูกส่งผ่าน GET จะรวมอยู่ใน URL ทำให้ผู้ใช้เปิดดูได้ง่าย เพียงแค่เปิด URL นั้น (อาจมีข้อจำกัดเรื่องขนาดและความปลอดภัย)
- เหมาะสำหรับการค้นหาข้อมูล, เปิดหน้าเว็บ หรือดึงข้อมูลที่ปลอดภัยต่อการเปิดเผย

### Post จับข้อความใส่มาแล้วส่งเลย เป็นการส่งข้อความของฟังก์ชันที่อยู่ข้างใน
> POST Method:
- ใช้สำหรับส่งข้อมูลไปยังเซิร์ฟเวอร์ เพื่อประมวลผล เช่น การส่งข้อมูลฟอร์ม, การอัพโหลดไฟล์, การสร้างหรือการเปลี่ยนแปลงข้อมูลเซิร์ฟเวอร์
- ข้อมูลที่ถูกส่งผ่าน POST จะอยู่ใน body ของคำขอ (request body) ทำให้สามารถส่งข้อมูลปริมาณมากได้และมีความปลอดภัยกว่าการแนบมากับ URL
- เหมาะสำหรับการส่งฟอร์มข้อมูล, การทำธุรกรรม, หรือการส่งข้อมูลที่ไม่ควรเปิดเผยใน URL

## Front End
### HTML (จัดรูปแบบหน้า)
- ```<DOCTYPE!>```
  > ส่วนที่ไม่ค่อยมีความสำคัญ เพียงแค่กำหนด
- ```<head>```
  > ส่วนที่เป็นหัวเว็บ ตัวอธิบายเว็บ คีย์เวิร์ดของเว็บ โลโก้ ส่วนที่ input สิ่งที่สำคัญๆ
- ```<body>```
  > ส่วนที่จะแสดงอยู่บนเว็บ

### CSS (ช่วย HTML ในการจัดหน้าให้สวยงาม)
- 1. Responsive web
  > เพิ่ม-ลด ขนาดของส่วนประกอบในหน้าเว็บ ตามเครื่องที่ใช้

- 2. Adaptive Web Design (AWD)
  > เว็บไซต์ประเภทนี้ใช้เลย์เอาต์แบบคงที่ที่ปรับไปตามขนาดหน้าจอที่กำหนดเป็นจุด ๆ (breakpoints) เว็บไซต์จะมีหลายเวอร์ชันที่ออกแบบมาสำหรับช่วงของขนาดหน้าจอเฉพาะ เช่น มือถือ แท็บเล็ต และเดสก์ท็อป ซึ่งแตกต่างจาก Responsive Design ที่เลย์เอาต์จะปรับโดยอัตโนมัติตามการย่อขยายของหน้าต่างเบราว์เซอร์

- 3. Static Web Design
  > เว็บไซต์นิ่ง (Static) มีเนื้อหาคงที่และแต่ละหน้าต้องออกแบบแบบแยกกัน ส่วนมากจะใช้ HTML และ CSS โดยไม่ต้องใช้ภาษาโปรแกรมฝั่งเซิร์ฟเวอร์ ทำให้เหมาะสำหรับเว็บไซต์ขนาดเล็กที่เนื้อหาไม่ค่อยเปลี่ยนแปลง

- 4. Dynamic Web Design
  > เว็บไซต์ไดนามิก (Dynamic) สามารถเปลี่ยนแปลงเนื้อหาได้ตามเงื่อนไขหรือเหตุการณ์ที่เกิดขึ้น เช่น การดึงและแสดงข้อมูลที่เปลี่ยนแปลงจากฐานข้อมูล ส่วนมากจะใช้ร่วมกับภาษาโปรแกรมฝั่งเซิร์ฟเวอร์ เช่น PHP, ASP.NET หรือ Java และฐานข้อมูล เช่น MySQL หรือ PostgreSQL

- 5. Single Page Application (SPA)
  > เป็นเว็บไซต์ที่โหลดหน้าเว็บเดียวและเปลี่ยนเนื้อหาภายในหน้านั้นโดยไม่ต้องรีโหลดหน้าทั้งหมด ส่วนมากจะใช้ JavaScript frameworks เช่น React, Angular หรือ Vue.js เพื่อให้การใช้งานที่ลื่นไหลและคล้ายแอปพลิเคชันบนมือถือ

- 6. Progressive Web App (PWA)
  > เป็นการผสมผสานระหว่างเว็บและโมบายแอปพลิเคชัน โดยเสนอลักษณะการทำงานที่คล้ายแอปมือถือ เช่น การเข้าถึงออฟไลน์ การแจ้งเตือนดัน และความสามารถในการติดตั้งบนอุปกรณ์มือถือ

- 7. Mobile-first Web Design
  > การออกแบบเว็บไซต์โดยเน้นที่การแสดงผลบนอุปกรณ์มือถือเป็นหลัก จากนั้นค่อยเพิ่มความซับซ้อนของเลย์เอาต์เมื่อหน้าจอใหญ่ขึ้น วิธีการนี้เน้นการให้ประสบการณ์ที่ดีที่สุดแก่ผู้ใช้บนมือถือก่อน

*แต่ละประเภทมีประโยชน์และความท้าทายที่แตกต่างกัน การเลือกประเภทที่จะใช้ควรพิจารณาจากวัตถุประสงค์ของเว็บไซต์และผู้ใช้งานเป้าหมายเป็นหลัก*

### JavaScript (ควบคุมการทำงาน การกดปุ่มของเครื่อง เพิ่มลูกเล่นให้กับหน้าเว็บ)
- เน้นการใช้งานบนฝั่งไคลเอนต์ (client-side) ของเว็บเบราว์เซอร์ ทำให้เว็บเพจสามารถตอบสนองต่อผู้ใช้และมีลักษณะการทำงานที่โต้ตอบได้ (interactive) มากขึ้น
- ใช้ในการพัฒนาเซิร์ฟเวอร์ (server-side) ผ่าน Node.js
- คุณสมบัติหลักของ JavaScript ได้แก่:
  > - Dynamic Typing: ไม่จำเป็นต้องระบุประเภทของข้อมูล (data type) เมื่อประกาศตัวแปร
  > - Prototype-based: การเขียนโปรแกรมเชิงวัตถุ (Object-Oriented Programming) ที่ใช้ต้นแบบเป็นพื้นฐาน
  > - Event-driven: รองรับการทำงานตามเหตุการณ์ (events) เช่น การคลิกเมาส์หรือการกรอกข้อมูล
  > - First-class Functions: สามารถใช้งานฟังก์ชันเป็นตัวแปร, ส่งผ่านฟังก์ชันไปยังฟังก์ชันอื่น และคืนค่าเป็นผลลัพธ์ได้

## Back End 
- ใช้ได้หลากหลายภาษา วิชานี้ใช้ Python เป็นหลัก

### Python
 Conda สามารถติดตั้งได้จาก
- **Miniconda** 👉 [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
- **Anaconda** 👉 [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)

```sh
conda --version #ตรวจสอบว่าติดตั้งสำเร็จหรือไม่?
```

#### Python Main Function 
- [https://www.geeksforgeeks.org/python-main-function/](https://www.geeksforgeeks.org/python-main-function/)
> Main Function ใช้ควบคุม flow ของ program โดยลำดับการทำงานจะทำตาม Main fc
> ดังนั้น จึงจำเป็นต้องมี Main function เพื่อที่เวลาเริ่ม program จะได้รู้ว่าต้อง run อะไรก่อน โดยดูจาก main func

```python
# Python program to demonstrate 
# main() function 

print("Hello") 

# Defining main function 
def main(): 
	print("hey there")  // have only process

# Using the special variable 
# __name__ 
if __name__=="__main__": 
	main()
```
Output  
> Hello  
> hey there

#### การรับ input จากภายนอก  
- [Argparse](https://docs.python.org/3/library/argparse.html)
- ใช้สำหรับการประมวลผลและจัดการกับอาร์กิวเมนต์และพารามิเตอร์ที่ส่งเข้ามาในบรรทัดคำสั่ง (command line arguments)
- ช่วยให้สามารถสร้างโปรแกรมที่สามารถรับอาร์กิวเมนต์จากผู้ใช้ได้อย่างสะดวกและใช้งานง่าย
- code ที่ดี ถ้าเสร็จแล้วไม่ควรมาแก้ซ้ำๆ ถ้าจะแก้แค่ input เฉยๆ
- คุณสมบัติหลักของ argparse ได้แก่:
  > - การกำหนดอาร์กิวเมนต์ที่ง่ายดาย: นักพัฒนาสามารถกำหนดอาร์กิวเมนต์ที่โปรแกรมจะรองรับได้อย่างง่ายดาย ทั้งชนิดของข้อมูล (เช่น string, int, float) และค่าเริ่มต้น เป็นต้น
  > - มีการตรวจสอบข้อผิดพลาด: argparse จะตรวจสอบว่าผู้ใช้ได้ส่งอาร์กิวเมนต์ที่ถูกต้องตามที่โปรแกรมกำหนดหรือไม่ และสามารถแสดงข้อความแนะนำวิธีการใช้งานโปรแกรม (help message) ได้โดยอัตโนมัติ
  > - รองรับพารามิเตอร์แบบ positional และ optional: สามารถกำหนดอาร์กิวเมนต์ที่จำเป็นต้องมี (positional) และอาร์กิวเมนต์ที่มีหรือไม่มีก็ได้ (optional)
  > - สร้างคำอธิบายอัตโนมัติ: สามารถสร้างคำอธิบายการใช้งานโปรแกรมและอธิบายอาร์กิวเมนต์ต่าง ๆ ที่โปรแกรมรองรับได้อย่างอัตโนมัติ

```python
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-t', "--time", default = 5)

args = parser.parse_args()
timet = int(args.time)
print(timet)

time.sleep(timet)
input("Press Enter to continue...")
time.sleep(timet)

print("Bye")
```
