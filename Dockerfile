FROM python:3.8
EXPOSE 8501

WORKDIR /streamlit-ipad

# Upgrade pip with no cache
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . /streamlit-ipad

RUN pip3 install -r requirements.txt

CMD streamlit run main.py --server.port=8501 --server.address='localhost'
