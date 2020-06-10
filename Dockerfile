FROM python:3

# Install scrapy and the spiders
RUN pip install scrapy
RUN mkdir /scrapy-cm
COPY cm /scrapy-cm/cm
COPY scrapy.cfg /scrapy-cm/scrapy.cfg
WORKDIR /scrapy-cm

# Set up the output folder:
RUN mkdir /CProject
ENV CPROJECT_FOLDER=/CProject

CMD [ "scrapy" ]
