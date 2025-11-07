# Project Kho Dữ Liệu (Data Warehouse) E-commerce Olist

Đây là một project Data Engineering (DE) end-to-end (từ đầu đến cuối), xây dựng một Data Warehouse hoàn chỉnh cho bộ dữ liệu Olist E-commerce (100k đơn hàng tại Brazil).

Project này mô phỏng quy trình ELT (Extract-Load-Transform) hiện đại, từ dữ liệu thô (CSV) đến một Dashboard phân tích kinh doanh.

## 🌟 Dashboard Kết Quả (Looker Studio)

Đây là sản phẩm cuối cùng, một dashboard phân tích 3 khía cạnh chính: Doanh thu, Tình trạng đơn hàng và Địa lý khách hàng.

![Hình ảnh Dashboard](LINK_ANH_DASHBOARD_CUA_BAN) 
*(Cách lấy link: Lên GitHub, vào repo, click "Add file" -> "Upload files", tải ảnh lên. Sau đó click vào ảnh đã tải lên và copy URL của nó)*

---

## 🏗️ 1. Kiến Trúc & Luồng Dữ Liệu

Project này sử dụng kiến trúc ELT. Dữ liệu được Tải (Load) vào kho thô trước, sau đó mới Biến đổi (Transform) bằng dbt.

Sơ đồ luồng dữ liệu (Data Lineage) được tự động tạo bởi `dbt docs`:

![Data Lineage Graph](LINK_ANH_DATA_LINEAGE_CUA_BAN)
*(Cách lấy link: Tương tự như ảnh Dashboard)*

---

## 🛠️ 2. Công Nghệ Sử Dụng

* **Kho dữ liệu (Data Warehouse):** PostgreSQL
* **Ngôn ngữ lập trình:** Python (cho phần Load)
* **Load Dữ liệu (Load):** Thư viện Pandas & SQLAlchemy
* **Biến đổi Dữ liệu (Transform):** **dbt (data build tool)**
* **Kiểm thử Dữ liệu (Testing):** `dbt test` (Kiểm tra unique, not_null, relationships)
* **Tài liệu hóa Dữ liệu (Docs):** `dbt docs`
* **Trực quan hóa (Visualize):** Google Looker Studio

---

## 📁 3. Cấu Trúc Project

```
MyFirstDEProject/
├── DataSet/               # Chứa 9 file .csv dữ liệu thô
├── Output_Data/           # Chứa 3 file .csv sạch (để tải lên Looker Studio)
├── olist_dwh/             # THƯ MỤC CHÍNH CỦA DBT
│   ├── models/
│   │   ├── staging/       # Lớp Staging: Làm sạch, đổi tên, ép kiểu
│   │   │   ├── stg_orders.sql
│   │   │   └── ...
│   │   ├── marts/         # Lớp Marts: Xây dựng Star Schema
│   │   │   ├── fact_orders.sql
│   │   │   ├── dim_customers.sql
│   │   │   └── dim_products.sql
│   │   └── sources.yml    # Khai báo nguồn dữ liệu thô
│   └── dbt_project.yml    # File cấu hình dbt
├── .gitignore             # File loại bỏ thư mục rác (target/, logs/)
├── load_raw_data.py       # Script Python để tải CSV vào Postgres
└── README.md              # File bạn đang đọc
```

---

## 🔧 4. Cách Chạy Lại Project

### Bước 1: Tải Dữ liệu Thô (Load)
1.  Tạo database PostgreSQL (ví dụ: `ecommerce_dwh`) và schema `raw`.
2.  Cài đặt thư viện Python: `pip install pandas sqlalchemy psycopg2-binary`
3.  Chỉnh sửa chuỗi kết nối `db_url` trong file `load_raw_data.py`.
4.  Chạy script: `python load_raw_data.py`.

### Bước 2: Biến đổi Dữ liệu (Transform)
1.  Cài đặt dbt: `pip install dbt-postgres`
2.  Chỉnh sửa file `olist_dwh/profiles.yml` (nằm ở `C:\Users\TenBan\.dbt\`) để trỏ đến database `ecommerce_dwh`.
3.  Di chuyển vào thư mục dbt: `cd olist_dwh`
4.  Chạy các models: `dbt run`
5.  Kiểm thử chất lượng: `dbt test`