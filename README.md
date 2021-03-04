# Overview
The purpose of the analysis was to deteremine the efficacy of a ice cream stand in Oahu, Hawaii by analyzing the temperatures and rain fall throughout the year.

# Results
The results were the following:
- June and December average temperatures only differ 3.9 degrees (5.5%).
- The minimum temperature for December was 8 degrees (8.8%) lower than June.
- Max temperature is only 2 degrees (2.4%) lower in December compared to June.

![June Temperature Stats](https://raw.githubusercontent.com/jdwrhodes/surfs_up/main/resources/JuneTemps.png 'June temperature stats')
![December Temperature Stats](https://raw.githubusercontent.com/jdwrhodes/surfs_up/main/resources/DecemberTemps.png 'December temperature stats')

# Summary
After studying the two months, Oahu would be an excellent candidate for an ice cream shop that's operating year round. The two month's temperatures deviate very little from each other. 

Two additional queries (in python) to study the precipitation for June and December would be:

```python
session.query(Measurement.prcp).filter(extract('month', Measurement.date) == 6)

session.query(Measurement.prcp).filter(extract('month', Measurement.date) == 12)
```
