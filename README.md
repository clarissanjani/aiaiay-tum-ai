# Brightly.AI
Description: To be able to implement effective environmental policies, it is critical to first understand how the environment is being used (e.g. industry, farming, forest). In many areas of the world, official data is lacking, meaning it is incredibly difficult to assess the true impact and thus to plan ahead.

Due to the increasing amount of satellite data, as well as improvements in computer vision, researchers have recently started to use AI to automatically determine land usage from space.


# Challenge

- Build a model that accurately predicts land usage from satellite image data using the [EuroSAT](https://github.com/phelber/EuroSAT) dataset
- Provide a compelling demo to showcase how the model works on a region of the world where land usage data is lacking – showing a downstream use case of land usage prediction!
- Provide a business plan & market analysis to turn this prototype into a startup

# Problem:
- Record highs in greenhouse gas emissions with electricity causing 73% of it
- Inefficient usage of unused land to harness renewable energy sources

# Solution:
Leveraging AI to analyze satellite imagery, our solution recommends the best areas to develop renewable energy sites so that farmers and governments have new plans of action to transition to sustainable energy sources such as wind and solar energy

# Key Features:
 - React frontend webpage with project vision -- check _aiaiay-app_ package 
 - React frontend dashboard with vision functionalities -- check _aiaiay-dashboard_
   - Recommendation system for energy solution according to processed data
 - Dash frontend with functional MVP -- check _scripts/dash_app.py_ 
   - Takes city name as input 
   - Runs backend with data processing
   - Outputs processed image according to input with algorithmic visualization
 - Python backend with data processing -- check _scripts_ and _notebooks_
   - NN trained for image classification based on [EuroSAT](https://github.com/phelber/EuroSAT) dataset
   - Google Maps API integration
   - Weather data pipeline 
 

# Folder Structure:
 - Packages:
   - _aiaiay-app_
   - _aiaiay-dashboard_
   - _scripts_
   - _notebooks_
 - Output and Files:
   - _ppt_ (Slide Deck + Business Model Canvas)
   - _html_ (Weather maps) 

Note: Use $ !pip3 install -r requirements.txt

# License and Copyright
© Leopold Wieser, Clarissa Anjani, Lilly Kaemmerling, Leonard Wolters, Juan Carlos Climent Pardo
