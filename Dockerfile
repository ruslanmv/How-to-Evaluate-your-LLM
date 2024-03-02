FROM python:3.9.18

RUN useradd -m -u 1000 user

USER user

ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app 

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt
EXPOSE 7860

ENTRYPOINT ["python", "src/manage.py", "runserver","0.0.0.0:7860"]