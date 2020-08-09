FROM python:3.8

RUN mkdir -p /workspaces/summer-code-jam-2020-2/festive-ferrets/frontend/code-jam/node_modules

VOLUME /workspaces/summer-code-jam-2020-2/festive-ferrets/frontend/code-jam/node_modules

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs

COPY festive-ferrets/requirements.txt .

RUN pip install -r requirements.txt

