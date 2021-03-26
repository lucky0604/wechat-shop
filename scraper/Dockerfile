FROM python:3.8

WORKDIR /app
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY ./requirements.txt /app/requirements.txt


RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /app/requirements.txt && rm -rf /root/.cache/pip


COPY . /app/
