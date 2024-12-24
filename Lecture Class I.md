# Command Line พื้นฐานบน Terminal
### 1. ระบุตำแหน่งปัจจุบันที่เราอยู่ในระบบ 
```
pwd
```
### 2. list ทุกๆ file/folder ที่อยู่ใน folder ปัจจุบัน 
``` 
ls
```
```
ls -l
```
```
ls -ltr #บอกรายละเอียดไฟล์อย่างละเอียด
```
### 3. สร้าง Folder
``` 
mkdir ชื่อของโฟลเดอร์
```
### 4. Change directory 
```
cd 
```
```
cd .. #ถอยกลับออกจากโฟลเดอร์ปัจจุบัน 1 ครั้ง
cd ../.. #ออกจากโฟลเดอร์ปัจจุบัน 2 ครั้ง
```
```
cd .xxx/yyy/zzz #เปลี่ยน directory แบบระบุปลายทาง
```
```
cd filename/ xxx #กรณีที่ชื่อไฟล์มี spacebar คั่น Ex. Class 4 ต้องพิมพ์ `cd Class/ 4`
```
### 5. Create file 
``` 
vi
vi {filename}  #สร้างและเปิดไฟล์
vi {filename.py} #python 
  #กด i เพื่อแก้ไข
  #กด esc + :wq (exit & save)
  #กด esc + :q! (exit but don't save)
```
### 6. Open file
```
cat filename #เวลาเราสั่งไม่จำเป็นต้องเข้าไปอยู่ใน folder นั้นๆ
```
### 7. Move file 
```
mv {ที่อยู่ต้นทางของ file/folder ที่ต้องการย้าย} {ที่อยู่ปลายทางที่ต้องการที่จะย้าย file/folder ไป}
mv file name .location
mv .xxxxx .zzzzzz #เป็นวิธีการเปลี่ยนชื่อรูปแบบหนึ่ง #Ex. mv ชื่อเก่า ชื่อใหม่
```
### 8. Copy file
```
cp {ที่อยู่ต้นทางของ file/folder ที่ต้องการคัดลอก} {ที่อยู่ปลายทางที่ต้องการที่จะคัดลอก file/folder ไป}
cp .zzzzzzz . #คัดลอกไฟล์มาที่โฟลเดอร์ปัจจุบัน
```
### 9. Manual page
```
man #ดูเอกสารคำสั่งและโปรแกรมต่าง ๆ ในรูปแบบ "หน้าคู่มือ" 
man ls #ใช้ดูรายการไฟล์ #ใช้ได้กับทุกคำสั่ง ที่เขาเขียน Instruction มาให้
```
### 10. Delete file
```
rm # ลบไฟล์
rm -r #.ให้มัน recursive ลบทุกไฟล์ที่มีอยู่ในโฟลเดอร์ เพื่อลบทั้งโฟลเดอร์
```
### 11. Check Systems Preference
```
htop #เอาไว้ดูว่ามี RAM อยู่เท่าไหร่ ดูการใช้งานของเครื่อง # ต้อง Install ก่อน
```
