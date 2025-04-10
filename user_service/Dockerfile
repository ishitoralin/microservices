# 使用官方 Python 基礎映像
FROM python:3.13-slim

# 設定工作目錄
WORKDIR /app

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式的代碼到容器
COPY . /app/

# 讓容器運行 FastAPI 應用
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
