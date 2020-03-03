#
#
#
FROM ubuntu
RUN apt-get update -q -y && \
    apt-get upgrade -y && \
    apt-get install -y python-pip && \
    pip install flask
COPY sample_temperature.py /

EXPOSE 8080

ENTRYPOINT ["python", "/sample_temperature.py"]
