# drill-phraseology
A tool that creates full drill phraseology based on the drill lesson of choice. This is to aid the tuition of British Army drill.

The idea is that you will be able to choose a drill lesson from a drop-down menu and that the template of drill phraseology will be filled in with the relevant words of command, points to note, etc.

# update

- Data is currently hard-coded
- Create page (and CRUD generally) not yet funtional

# requires
python 3.5.2
python3-virtualenv
mongodb
flask
pymongo

# recommended start-up procedure
- fork/clone repo
- create virtual environment `virtualenv -p python3 venv`
- activate virtual environment `source venv/bin/activate`
- install packages `pip install flask pymongo`
- run server from virtual environment `python phraseology.py`
