FROM python:3

LABEL maintainer="729263226@qq.com"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python","app.py"]
