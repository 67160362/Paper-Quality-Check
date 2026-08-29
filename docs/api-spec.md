# API Spec — Phase 1

Phase 1 มี endpoint สำหรับตรวจสถานะระบบเท่านั้น:

- `GET /api/health` — คืนค่า `{ "status": "ok", "phase": 1, "database": "mock" }`

REST endpoints สำหรับ auth, lots, quality, reports, products, quality items และ users จะเพิ่มใน Phase 3–6

