## UK EV Data Analysis

Analysis of Electric Vehicle charging infrastructure in the United Kingdom.

### Retrieve Data

You can use the [moatsystems_get_ev_data.py](./moatsystems_get_ev_data.py) code to retrieve data from [EVPlugs API](https://moatsystems.com/evplugs-api/). Running the file generates a JSON file for analysis.

```python
## Prerequisites
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 moatsystems_get_ev_data.py
deactivate
```

### Run Notebook

You can run the notebook live on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/moatsystems/uk_ev_data_analysis/main?filepath=moatsystems_ev_data_analysis.ipynb)

### Authors

- **Finbarrs Oketunji** _aka 0xnu_ - _Product Owner_ - [0xnu](https://github.com/0xnu)

### License

The script is published under [WTFPL License](LICENSE).

### Copyright

(c) 2022 [Moat Systems Limited](https://moatsystems.com).