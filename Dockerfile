FROM python:3.8

RUN  mkdir -p  /streamlit_ipad
COPY . ./streamlit-ipad
WORKDIR /streamlit-ipad

#### Use this work ####
RUN  mkdir -p  /streamlit_ipad
WORKDIR /streamlit-ipad
COPY . .
######################
# Upgrade pip with no cache
RUN apt-get update && apt-get install -y git

RUN pip3 install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["main.py", "--server.address=0.0.0.0", "--server.port=8501"]
