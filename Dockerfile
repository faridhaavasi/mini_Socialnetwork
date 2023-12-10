FROM python
WORKDIR /src
COPY requirments.txt /src
EXPOSE 8000
RUN pip install -r requirments.txt
COPY . /src


