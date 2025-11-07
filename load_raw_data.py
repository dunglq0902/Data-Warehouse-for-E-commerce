import pandas as pd
from sqlalchemy import create_engine
import os

# --- 1. CẤU HÌNH ---

# Cập nhật chuỗi kết nối của bạn:
# postgresql://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DATABASE_NAME]
# (Nếu chạy ở máy bạn thì host là localhost, port thường là 5432)
db_url = "postgresql://postgres:090205@localhost:5432/ecommerce_dwh"

# Đường dẫn đến thư mục chứa 9 file CSV
data_dir = r"D:\MyFirstDEProject\DataSet" # Chữ r ở đầu rất quan trọng!

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

    # Lặp qua từng file
    for file_name in files_to_load:
        # Tạo tên bảng từ tên file
        # 'olist_customers_dataset.csv' -> 'raw_customers'
        table_name = "raw_" + file_name.replace('olist_', '').replace('_dataset', '').replace('.csv', '').replace('product_category_name_translation', 'product_category_name_translation')
        
        file_path = os.path.join(data_dir, file_name)
        
        print(f"Đang xử lý file: {file_name}  ->  Đang tải vào bảng: {table_name} ...")
        
        # Đọc CSV bằng Pandas
        df = pd.read_csv(file_path)
        
        # Dùng Pandas để TỰ ĐỘNG TẠO BẢNG và INSERT DỮ LIỆU vào schema 'raw'
        df.to_sql(
            table_name,         # Tên bảng sẽ được tạo
            engine,             # Kết nối database
            schema='raw',       # Chỉ định schema 'raw'
            if_exists='replace', # 'replace' = Xóa bảng cũ nếu tồn tại và tạo lại.
                                # (Dùng 'fail' nếu bạn muốn nó báo lỗi nếu bảng đã tồn tại)
            index=False         # Không chèn cột index (số thứ tự) của Pandas
        )
        
        print(f"✅ Tải thành công bảng: {table_name}")

    print("\n🎉 Hoàn thành! Tất cả 9 file đã được tải lên schema 'raw'.")

except Exception as e:
    print(f"❌ Đã xảy ra lỗi: {e}")