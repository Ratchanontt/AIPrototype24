# Virtual Machine

### 1. การเข้า Server ด้วย `ssh ย่อมาจาก Secure Shell` `#คิดเหมือนเปลือกหอย ค่อยๆ หุ้ม ค่อยๆ เข้า`
```
ssh username@IPaddress
```

### 2. เพิ่ม `User` เพื่อนให้เข้า server ของเราได้
```
sudo adduser friendusername
```

### 3. ใช้ดูการเคลื่อนไหวใน server ของเรา
```
htop
```

### 4. ย้าย group
```
sudo usermod ชื่อเพื่อน ชื่อเรา #ชื่อเพื่อน = group ชื่อเรา = folder
```
```
sudo groups ชื่อเรา #เช็คว่ามีใครอยู่ใน server
```

### 5. เพิ่มเพื่อนให้เป็น SuperUser Do `sudo`
```
sudo adduser ชื่อเพื่อน sudo 
```




