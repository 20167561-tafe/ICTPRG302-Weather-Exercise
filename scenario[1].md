Today, we're building a simple weather data analysis app in teams. Some skeleton
code has been provided, and a data file. For the purposes of the exercise, leave
the data file as you've found it. You can pull similar data from the BOM:
https://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p\_nccObsCode=122\&p\_display\_type=dailyDataFile\&p\_stn\_num=009225\&p\_startYear=2025\&p\_c=-17025626

Data for min temperature, max temperature, and rainfall have been combined together.

Your team will need to implement several features, and you can work in parallel
by using Git and GitHub. Select someone from the team to own the primary GitHub
repo. That person should put a copy of the skeleton code and data into a new repo.
Everyone else should take a fork and begin working on their assigned feature. The
owner should work in a feature branch so that all changes will be merged by pull
request.

Issue one pull request per feature! Try developing the first 3 items in parallel,
but use the code your team has yet to complete: variance should reuse the mean
calculation, and standard deviation should reuse the variance calculation. This
will make testing your code tricky! See if you can think of some ways around this
problem.

The features to be implemented are:

1. Implement a mean calculation (Chris)
2. Implement a variance calculation (Chao)
3. Implement a standard deviation (Faisal)
4. Implement a range calculation (Duva)
5. Implement an interquartile range calculation (Chris)
6. Extend the menu to collect a date range from the user (if desired) (Chao)
7. Extend the menu to collect a desired statistical calculation (Faisal)
8. Extend the menu to answer the user's questions until they choose to quit (Duva)
9. Implement a date filter on the requested data series (Chris)
10. Add an another data series: temperature range. It should be calculated from max-min temperature.

