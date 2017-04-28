# FairEstimate - A RideShare Comparison Interface
Web Application using flask and Google/Uber APIs to compare and visualize real-time cost and trip duration estimates for Uber vs. Taxis in NYC

DESCRIPTION:
This package consists of all the necessary code and information about "FairEstimate",
a web application designed to compare the best rideshare to use at any given time. The contents of this package are split up into two parts:
  
    1. DOC:
        - Our team's final report describing our proposed methods, algorithms, experiments, evaluations, interface, and conclusions. It outlines why we took the steps we did and what we accomplished by doing so.
        - Our team's final poster that gives a brief summary of the project and the most important findings.

    2. CODE:
        - Important pieces of code involved in the project. This includes:
            1. app.py - the script that you will run in terminal to generate the local host which displays the interface (uses Uber API)
            2. reg.py - a helper script for app.py that computes taxi fare estimate based on the linear model we've created
            3. LM.csv - a list of linear regression model coefficients for each subset of the data
            4. templates/index.html - the HTML/CSS/JS file that the interface is built upon (uses Google Maps JavaScript API)
            5. parser.py - Parses through Taxi Dataset into different subsets depending on type and time of the day
            6. lmcreater.R - Create the model to estimate taxi fares
            7. test.R - Testing script for the different algorithms used such as neural networks and kNN.

INSTALLATION (includes model building):
    
    1. Download the January 2016 Yellow NYC Taxi Dataset from the following link:   http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml
    2. Sign up for Uber and Google Maps API server tokens
    3. Use Python 2.7+
    4. Necessary R packages to install: ggplot2, nnet
    5. Necessary Python packages to install: uber_rides, flask, flask-bootstrap, flask_wtf, urllib2, WTForms (should be as simple as running "pip install _____")
    6. Lastly, store index.html in a folder called "templates" in the same directory as the other code.


EXECUTION:
    
    1. Run "python app.py" from terminal/command line. It will generate a local host (something like http://127.0.0.1:5000) for you to copy and paste into your address bar in Chrome. Add "/table" to the end of the local host (so you should be putting http://127.0.0.1:5000/table into the address bar)
    2. Enter your desired starting/ending locations into the input field. Click "Calculate" and wait for the results to generate.
