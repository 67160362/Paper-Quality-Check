# PaperGuard

PaperGuard — Smart Paper Quality Control System สำหรับตรวจสอบคุณภาพกระดาษในแต่ละ Production Lot

## Phase 1

เวอร์ชันนี้เป็น demo ที่มี UI หลัก, mock data, responsive layout และ automatic PASS/FAIL logic ในหน้า Quality Check โดยยังไม่เชื่อม PostgreSQL จริง

## Features

- Login ด้วย demo accounts และ role label
- Dashboard พร้อม KPI, production chart, quality summary และ alerts
- Production Lots พร้อม search, filter UI และ navigation ไป Quality Check
- Quality Check คำนวณ PASS/FAIL จากค่า measured เทียบกับ minimum/maximum
- Responsive sidebar สำหรับ desktop และ mobile

## Tech Stack

- Frontend: HTML, CSS, Vanilla JavaScript
- Backend: Python, FastAPI
- Development: Docker Compose
- Database: เตรียมโครงสร้างสำหรับ Phase 4 (ยังใช้ mock data)

## How to Run

สำหรับการพรีเซนต์แบบ Demo อย่างเดียว ให้ push ขึ้น branch `main` แล้วเปิดเมนู `Settings → Pages` เลือก `GitHub Actions` จากนั้น workflow จะ deploy โฟลเดอร์ `frontend` ให้อัตโนมัติ เปิด URL ที่ GitHub แสดง แล้วใช้หน้า `demo.html`

```bash
docker compose up --build
```

เปิด [http://localhost:8000](http://localhost:8000) และ Swagger ที่ [http://localhost:8000/docs](http://localhost:8000/docs)

ถ้าต้องการรันโดยไม่ใช้ Docker:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Demo Accounts

| Role | Username | Password |
|---|---|---|
| QC Staff | `qc01` | `password` |
| Supervisor | `supervisor01` | `password` |
| Admin | `admin01` | `password` |

## Demo Test

1. Login ด้วย `qc01 / password`
2. ไปที่ Production Lots และเลือก `LOT-2026-001`
3. กด Quality Check แล้วตรวจค่าตั้งต้น: `80, 6, 101, 320` → PASS
4. เปลี่ยน Moisture เป็น `12` → FAIL พร้อมแจ้งรายการที่ไม่ผ่าน

## Next Phase

Phase 2 จะเพิ่ม validation/error states ที่ละเอียดขึ้นและรวมผลตรวจเข้า mock state ของ lot/history ก่อนเริ่มสร้าง REST API เต็มรูปแบบใน Phase 3
