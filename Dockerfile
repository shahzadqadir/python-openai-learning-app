FROM python:3.13

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN useradd -m script

USER script

WORKDIR /home/script/workspace

EXPOSE 8000

CMD ["sleep", "infinity"]