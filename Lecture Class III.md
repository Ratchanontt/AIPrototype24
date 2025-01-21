# Ubuntu on Cloud VM
## 1. Create VM 
เข้า Portal Azure >>> Education >>> VM >>> Create a virtual machine

## 2. Login & Logout
```
ssh username@IP #login
exit #logout /// จบ section
```

## 3. ออกจาก function ex. python
```
exit()
```

## 4. scp = secure copy 

- รูปแบบ
  ```
  scp {path ต้นทาง} {path ปลายทาง}
  ```

- ส่งไฟล์จากเครื่องเราไปบน Cloud (ต้องรันบนเครื่องเรา)
  ```
  scp ./xxx nnnt@IP:~/xxx/xxx/. Ex. scp ./testcode.py nnnt@4.221.171.101:~/code/.
  scp -r testfolder1/ nnnt@IP:~/nnnt/. # cp folder in PC to Cloud
  ```

- ดึงไฟล์จาก cloud มาเครื่องเรา (ต้องรันบนเครื่องเรา)
  ```
  scp nnnt@IP:/xxx/xxx/yyy.py /home/nnnt
  scp nnnt@4.221.171.101:/home/nnnt/code2/newtest.py /Users/macbookair # move file from folder name code2  on nnnt Cloud to PC
  ```

## 5. Session
```
screen -S {screen name} #สร้าง
```
```
screen -R #กระโดดกลับเข้่าไปที่ screen
```
- กด control A+D ออกจาก session
- กด control A+K+y ออกและลบ session

## 6. Github
  - Save code on github
  ```
  git clone https://github.com/Ratchanontt/AIPrototype24.git
  git add testcloudvm.py
  git commit -m "test cloud server"
  git push
  ```
  - Check Status
  ```
  git status
  ```
  - Setting owner Github (ทำครั้งเดียว)
  ```
  git config --global user.name "Ratchanontt"
  git config --global user.email "ratchanont.t@kkumail.com"
  ```

