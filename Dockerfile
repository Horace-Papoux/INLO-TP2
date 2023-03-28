FROM python:3.9

RUN useradd papou

RUN usermod -aG sudo papou

USER papou

WORKDIR /code

COPY ./setup.py /code/setup.py

COPY ./requirements.txt /code/requirements.txt

COPY ./README.md /code/README.md

COPY ./src /code/src

RUN sudo pip install /code

COPY ./controller /code/controller

CMD ["uvicorn", "controller.controller:app", "--host", "0.0.0.0", "--port", "80"]
