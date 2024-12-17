FROM python

WORKDIR /root/Yuri

COPY . .

RUN pip3 install --upgrade pip setuptools

RUN pip3 install -U -r requirements.txt

CMD ["python3", "-m", "Yuri"]
