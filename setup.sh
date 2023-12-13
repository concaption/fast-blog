#!/usr/bin/env bash

### Sets up python packages in for devcontainer.json

#create a virtualenv
python3 -m venv .venv


# append it to bash (if not there) so every shell launches with it
[[ $(tail -n1 ~/.bashrc) != 'source .venv/bin/activate' ]] && echo 'source .venv/bin/activate' >> ~/.bashrc

# source virtualenv
source .venv/bin/activate

# install all software
make install
