# Managing Environment Conda
 Conda สามารถติดตั้งได้จาก
- **Miniconda** 👉 [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
- **Anaconda** 👉 [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
```sh
conda --version #ตรวจสอบว่าติดตั้งสำเร็จหรือไม่?
```

## Create Environment
```sh
- conda create --name {ชื่อ env} python = {versionที่ต้องการ} #สร้าง Environment ใหม่
- conda create -n myenv {name of packager}
- conda activate {ชื่อ env} #เข้าใช้งาน
- conda deactivate #เลิกใช้งาน
- conda remove --name ai_project --all #ลบ Environment
- conda install {ชื่อpackage}
```

## Install package
> อยู่ใน VM และเข้า env แล้ว
```sh
- conda install {envi name}
- conda install pandas
```

