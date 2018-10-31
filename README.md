# amazon
Sentiment Analysis on Amazon user reviews.

## Usage
1. create a virtual environment
2. Install packages using requirements.txt 
3. Go to python Console
4. nltk.download('vader_lexicon')
5. nltk.download('gutenberg')
6. Install R 
7. Check if R runs in Command Line
8. Install Rvest library in R
9. Open R in Cmd
10. install.packages('rvest')
11. If fails sudo apt-get install libxml2-dev
12. python manage.py runserver
13. go to http://127.0.0.1:8000/scrape/data/ (Check Issues below if this fails)
14. To view old results go to http://127.0.0.1:8000/analyse/data/

## Current Issues
This code is written to scrape the reviews from Amazon product pages. The scrape code no longer works, maybe due to change in Website, you need to fix this to make this project fully working.

To test this quickly, delete the contents in the userReviews.txt and paste few reviews into userReviews.txt in similar format as before.

## What is Sentiment Analysis?

![Alt text](images/sa.png?raw=true "Sentiment Analysis")

## Existing System
The existing system shows top positive and negative reviews, but these are of overall product. We still need to search for the specific feature we are looking for in the product, for example, if we are looking for a mobile which has good camera, but the mobile is rated bad due to its battery problem. There is no simple way to identify this, unless we manually read the reviews.

![Alt text](images/existing.png?raw=true "Existing System")

## Proposed System
We should have an option to search for specific feature of the product, for example we should be able to search for the reviews related to camera only of a particular mobile device.

![Alt text](images/proposed.png?raw=true "Proposed System")

## Modules
The problem can be solved by dividing into two modules as below
![Alt text](images/modules.png?raw=true "Modules")

## Architecture 
The architecture of the project is 
![Alt text](images/architecture.png?raw=true "Architecture")

## Results
The final results are
![Alt text](images/results.png?raw=true "Results")

## Conclusion
![Alt text](images/conclusion.png?raw=true "Conclusion")