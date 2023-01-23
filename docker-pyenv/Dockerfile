FROM ubuntu:20.04


RUN apt-get update -y 

ENV TZ=Etc/UTC
#RUN DEBIAN_FRONTEND=noninteractive 

RUN apt-get install -y --no-install-recommends tzdata
RUN apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget ca-certificates curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev mecab-ipadic-utf8 git
RUN rm -rf /var/lib/apt/lists/*

ENV PYENV_ROOT "/pyenv"


ENV PYTHON_VERSION 3.10.9

RUN set -ex \
    && curl https://pyenv.run | bash 
ENV PATH "$PYENV_ROOT/bin:$PATH"
RUN eval "$(pyenv init -)"
RUN eval "$(pyenv virtualenv-init -)"

RUN pyenv update \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && pyenv rehash

ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"