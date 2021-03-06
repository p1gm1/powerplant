# powerplant
-------------------------------------------------------------------------------------

This project was made using this <a href="https://www.kaggle.com/gova26/airpressure">dataset</a>, it contains 9568 data points collected from a Combined Cycle Power Plant over 6 years (2006-2011), when the power plant was set to work with full load. Features consist of hourly average ambient variables Temperature (T), Ambient Pressure (AP), Relative Humidity (RH) and Exhaust Vacuum (V) to predict the net hourly electrical energy output (EP) of the plant. A combined cycle power plant (CCPP) is composed of gas turbines (GT), steam turbines (ST) and heat recovery steam generators. In a CCPP, the electricity is generated by gas and steam turbines, which are combined in one cycle, and is transferred from one turbine to another. While the Vacuum is colected from and has effect on the Steam Turbine, the other three of the ambient variables effect the GT performance.

The averages were taken from various sensors located around the plant that record the ambient variables every second.

This app uses a model trained with the alogrithm gradient boosting regresor, with a lost of 0.002. It operates well in these conditions:

* Temperature (T) in the range 1.81°C and 37.11°C
* Ambient Pressure (AP) in the range 992.89-1033.30 milibar
* Relative Humidity (RH) in the range 25.56% to 100.16%
* Exhaust Vacuum (V) in the range 25.36-81.56 cm Hg

### You can find the website in this URL https://www.powerplantml.com/

-------------------------------------------------------------------------------------
## Disclaimer
-------------------------------------------------------------------------------------

This app was made by Alberto Perdomo Mechanical Engineer, it can be used by anyone free of cost and it should only be used as guide to estimate the net hourly electrical energy output of a combined cycle power plant with similar conditions as the ones shown above.
