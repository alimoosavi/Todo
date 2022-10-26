FROM ubuntu:20.04

RUN apt-get -y update \
  && apt-get --no-install-recommends -y install \
  python3 \
  python3-dev \
  python3-pip \
  build-essential \
  && rm -Rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

RUN mkdir -p /opt/todo/

ADD ./requirements.txt /opt/todo/

WORKDIR /opt/todo/

RUN pip3 install -r requirements.txt

ADD . /opt/todo/

RUN chmod +x entrypoint.sh

EXPOSE 8000

CMD ./entrypoint.sh