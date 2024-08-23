import os
import json

# Đường dẫn đến thư mục chứa các tệp PNG
png_folder = 'D:/Working/Study/KHoi/zizi/mk/assets/img'

# Đường dẫn đến thư mục lưu trữ các tệp JSON
json_folder = 'D:/Working/Study/KHoi/zizi/mk/assets/data'


# Đường dẫn đến tệp cấu hình
config_path = 'config/generate_config.json'

# Đảm bảo thư mục JSON tồn tại
os.makedirs(json_folder, exist_ok=True)

# Xóa tất cả các tệp trong thư mục json_folder
for file_name in os.listdir(json_folder):
    file_path = os.path.join(json_folder, file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)

# Dữ liệu mẫu để điền vào các tệp JSON
default_icons = [
    {
    "x" : 1.042043486750081,
    "y" : 0.17915786985560564,
    },
    {
    "x" : 1.039438467980305,
    "y" : 0.11348760195044501,
    },
    {
    "x" : 1.043693420995539,
    "y" : 0.22617172461133794,
    }
]

# Đọc cấu hình từ tệp JSON
with open(config_path, 'r') as config_file:
    config_data = json.load(config_file)

# Đọc tất cả các tệp PNG trong thư mục
for filename in os.listdir(png_folder):
    if filename.lower().endswith('.webp'):
        # Tạo tên tệp JSON dựa trên tên tệp PNG
        json_filename = filename.replace('.webp', '.json')
        json_path = os.path.join(json_folder, json_filename)

        # Lấy cấu hình cho tệp PNG
        config = config_data.get(filename, {"icon": 1, "sounds": ["x"], "count": 1})

        # Lấy số lượng icon và âm thanh từ cấu hình
        icon_index = config["icon"]
        sounds = config["sounds"]
        count = config["count"]

        # Chọn số lượng item từ default_icons
        icons = []
        for i in range(min(count, len(default_icons))):
            icon = default_icons[i].copy()
            # Gán âm thanh cho mỗi icon
            icon["sound"] = sounds[i] if i < len(sounds) else "x"
            icons.append(icon)

        # Tạo dữ liệu JSON
        json_data = {
            "background": f"{filename}",
            "icons": icons,
            "backgroundSize": {
                "width": 554.8127177700349,
                "height": 730
            }
        }

        # Lưu dữ liệu JSON vào tệp
        with open(json_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

print(f"JSON files created in {json_folder}")
