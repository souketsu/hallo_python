import os
import csv
from datetime import datetime

class HistoryLogger:
    def __init__(self):
        self.history = []  # 历史记录列表
        self.txt_path = os.path.join("logs", "history.txt")  # TXT 文件路径
        self.csv_path = os.path.join("logs", "history.csv")  # CSV 文件路径

    def add(self, record):
        # 添加一条历史记录，带时间戳
        self.history.append(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {record}")

    def save_to_txt(self):
        # 保存历史记录到 TXT 文件
        with open(self.txt_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(self.history))

    def save_to_csv(self):
        # 保存历史记录到 CSV 文件
        with open(self.csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["时间", "表达式"])
            for record in self.history:
                timestamp, expression = record.split("] ", 1)
                writer.writerow([timestamp.strip("["), expression])
