import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv # <-- Thư viện mới

# --- 1. TẢI BIẾN MÔI TRƯỜNG ---
load_dotenv() # Tự động tìm và đọc file .env

# Lấy thông tin từ file .env
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")

# Kiểm tra xem có lấy được không (nếu không lấy được, báo lỗi)
if not all([db_user, db_password, db_host, db_port, db_name]):
    print("LỖI: Không tìm thấy một hoặc nhiều biến môi trường trong file .env")
    print("Vui lòng tạo file .env với các biến: DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME")
    exit() # Dừng chương trình

# Tạo chuỗi kết nối từ các biến
db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Đường dẫn đến thư mục chứa 9 file CSV
data_dir = r"...\Data-Warehouse-for-E-commerce\DataSet" 

# Tên 9 file CSV của bạn
files_to_load = [
    'olist_customers_dataset.csv',
    'olist_geolocation_dataset.csv',
    'olist_order_items_dataset.csv',
    'olist_order_payments_dataset.csv',
    'olist_order_reviews_dataset.csv',
    'olist_orders_dataset.csv',
    'olist_products_dataset.csv',
    'olist_sellers_dataset.csv',
    'product_category_name_translation.csv'
]

# --- 2. TỰ ĐỘNG CHẠY ---
try:
    engine = create_engine(db_url)
    print("Kết nối database thành công!")

    # (Phần còn lại giữ nguyên...)
    for file_name in files_to_load:
        table_name = "raw_" + file_name.replace('olist_', '').replace('_dataset', '').replace('.csv', '').replace('product_category_name_translation', 'product_category_name_translation')
        file_path = os.path.join(data_dir, file_name)

        print(f"Đang xử lý file: {file_name}  ->  Đang tải vào bảng: {table_name} ...")

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            engine,
            schema='raw',
            if_exists='replace',
            index=False
        )

        print(f"✅Tải thành công bảng: {table_name}")

    print("\n🎉 Hoàn thành! Tất cả 9 file đã được tải lên schema 'raw'.")

except Exception as e:
    print(f"❌ Đã xảy ra lỗi: {e}")