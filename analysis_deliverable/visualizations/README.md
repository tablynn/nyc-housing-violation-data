**Why did you pick this representation?**
We picked the map visualization because our dataset has a geographic component to it and we wanted to represent this visual component as we could not in our hypothesis testing/machine learning models. We were curious to see if there were geographic patterns in the violations that could be ascertained quickly from a map. 
We picked the stacked bar chart as we thought it would best represent the disparities between the total violations per year for high
income households versus for low income violations for each year. We had total quantities for two categories over several years.
A bar chart seemed most appropriate here. 
**What alternative ways might you communicate the result?**
There aren’t a lot of other ways to communicate geographic information for the map. This information could be conveyed via a graph where the nodes are zipcodes and the edges represent sharing a border with another zipcode. The size of the nodes could we weighted depending on the number of violations. 
We could have possibly used line graphs instead of a bar chart to depict total violations per year to compare the different trends for high income versus low income zipcodes. 
**Were there any challenges visualizing the results, if so, what where they?**
There were some challenges in navigating the structure and limitations of the plotly configuration of a chloropleth map. There was not a built-in structure for being able to divide a geographic region by zipcode so we needed to import a geoJSON that marked the boundaries of each zipcode and then lay the counts over this data. 
One other major challenge that we encountered that was less resolveable was the non-uniform distribution of the data making the color visuals of the map less impactful. Since the data ranges from a count of violations from 0 to 108, this was the default scale for the map. However, all but one of the data points fall within the scale of 1-40 violations, so the default scale for the map made if much more difficult to discern smaller differences in violations that were more common. Manually changing the range of the visual improved this, but we could not change the labelling of the legend.
There weren't a lot of challenges in creating the bar chart. We just had to create a separate table depicting total violations per year for high income versus low income zipcodes
**Will your visualization require text to provide context or is it standalone (either is fine, but it’s recognized which type your visualization is)?**
Both our visualizations could pretty much stand alone with a title. 
