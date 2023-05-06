FROM registry.fedoraproject.org/fedora-minimal

EXPOSE 5000

RUN microdnf -y install python-pip && microdnf clean all
COPY ./app /app

WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
