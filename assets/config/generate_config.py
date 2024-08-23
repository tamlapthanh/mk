import json

# Đường dẫn đến tệp cấu hình
config_path = 'config/generate_config.txt'

# Đường dẫn đến tệp JSON đầu ra
output_json_path = 'config/generate_config.json'

# Đọc cấu hình từ tệp văn bản
config_data = {}
with open(config_path, 'r') as config_file:
    for line in config_file:
        line = line.strip()
        if not line:
            continue
        file_part, icon_part, sounds_part, count_part = line.split(',')
        file_name = file_part.strip()
        icon = int(icon_part.strip())
        sounds = list(map(str, sounds_part.split(';')))
        count = int(count_part.strip())
        config_data[file_name] = {
            "icon": icon,
            "sounds": sounds,
            "count" : count
        }

# Lưu dữ liệu cấu hình vào tệp JSON
with open(output_json_path, 'w') as json_file:
    json.dump(config_data, json_file, indent=4)

print(f"Configuration JSON file created at {output_json_path}")
