How many data points are there in total? How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)? Aim for a resource of reasonable size. At least 500 records after cleaning and duplicate removal. Account that part of your data should be used for validation of your results only. Do you think this is enough data to perform your analysis later on?
For the list of massage spa locations we currently have 3,154 data points. We think that this will be more than enough to cross reference with the DOB data, and given that we have yet to merge the two datasets, we do expect we will have enough data points to work with. 
In the merged housing violations CSV we have 1,798 rows of addresses to housing violations to merge with the massage spa location dataset. 

What are the identifying attributes?
For the spa location datasets the identifying attributes are the name of the spa, the street address, and zip code
For the merged housing dataset, the identifying attributes are the house number and street for each row.
Where is the data from?
The housing violation data is from the New York Department of Buildings, published by the city of New York 
The spa location data is from Rubmaps, a site intended to help users find places that conduct massage therapy/sex work

How did you collect your data?
We collected the data using both scraping and APIs. We scraped the name and address from Rubmaps and retrieved all relevant information from the DOB websites through APIs. 

Is the source reputable?
We deemed the housing code violation data to be reputable as it is published by the NYC government
While we wouldn’t regard Rubmaps as a traditionally reputable source of data, we believe that for the purposes of this project, it provides the best way to obtain records of places of work that sex can be bought. For the analyses we are conducting, the data that Rubmaps provides does not have to be all-encompassing, and we do not interpret it as such. 

How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?
The data obtained from Rubmaps may exhibit some sort of sampling bias because it was not necessarily collected in a uniform way for the purposes of data collection. Because it is comprised of listings, there may be bias towards places of work that have users that are online/have awareness of Rubmaps as a platform. 

Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)
Because the nature of the data is revealing the addresses of places in which sex work might be conducted, there are considerations for the privacy of these places as we conduct our research. We want to make sure that when we publish our project, that our data is not accessible to the public and that individual data points are not identifiable. 

How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)

How did you check for the cleanliness of your data? What was your threshold reference?
One aspect of the data that had to be cleaned was the addresses. The addresses scraped off of Rubmaps were formatted very differently from the addresses on the DOB websites, which were all in different columns (street name, house number, zip code, etc). They also had inconsistencies with naming conventions (i.e. “street” vs “st”)

Did you implement any mechanism to clean your data? If so, what did you do?
We did some manual cleaning in order to separate house numbers from street addresses from zip codes and wrote code in order to normalize the Rubmaps addresses where abbreviations occurred. 
We are also using Google Maps geocoding API in order to normalize both datasets’ street addresses from there. 
Are there missing values? Do these occur in fields that are important for your project's goals?
With both datasets standing separately, there are not missing values. However, in utilizing Google Maps API, the street addresses occasionally turn to missing values when the API cannot convert them. These values will be dropped in the merged dataset. 

Are there duplicates? Do these occur in fields that are important for your project's goals?
There are definitely duplicates in the names of the spas. However, this will not be important in affecting our projects goals. 
How is the data distributed? Is it uniform or skewed? Are there outliers? What are the min/max values? (focus on the fields that are most relevant to your project goals)
Because our data is primarily spatial, we have not yet determined its distribution given that we have not mapped it using geospatial software

Are there any data type issues (e.g. words in fields that were supposed to be numeric)? Where are these coming from? (E.g. a bug in your scraper? User input?) How will you fix them?
Because street addresses from Rubmaps are not standardized, there are data type issues in standardizing the address. For example, in obtaining the house number, there are sometimes apartment numbers with letters appended to the house number. 
We are in the process of using the Google Maps API to standardize the street addresses

Do you need to throw any data away? What data? Why? Any reason this might affect the analyses you are able to run or the conclusions you are able to draw?
Currently we have two datasets that we will be able to map and compare spatially as well as do analyses with separately. 
In merging the datasets to do a concurrent analysis, we will lose a large majority of the data because our new dataset will be the spas that have housing code violations. By nature of the fact that only a portion of them will have violations, this dataset will be far smaller than either of the datasets separately as the merge itself will prove/reject a hypothesis. 
Because Rubmaps does not have a standard format for addresses, there will be additional data lost to the inability of the Google Maps API to convert the Rubmaps address 

Summarize any challenges or observations you have made since collecting your data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. (approximately 3-5 sentences)
Our primary challenge has definitely been normalizing the street addresses from Rubmaps. Our next steps would be using the Google Maps API to normalize the cleaned street addresses and the NYC Open data and merge the datasets for the smaller analysis of finding spas with housing violations. Because the street address data was far more difficult to clean than we had expected, we anticipate that the focus of our project will shift from this merged dataset to  



