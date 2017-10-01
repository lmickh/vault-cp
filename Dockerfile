FROM alpine:3.6

RUN apk add --update python3
COPY . /src/
RUN pip3 install -r /src/requirements.txt
CMD ["python3", "/src/vault-cp.py"]
