# Election Analysis

## Overview
This analysis uses Python to obtain the 2018 election results for the House of Representatives Race in the 1st District in Colorado. In this analysis I use for loops, conditionals to read a CSV file with the data and print the election outcomes to a text file. 


## Election-Audit Results
I wanted to find how many votes were cast, the number of votes each candidate received, the percentage of the total votes each candidate received, the number of votes by county and the percentage of the vote by county. 

* Total Votes Cast in the Election: 

    ![Screen Shot 2021-05-09 at 5 18 30 PM](https://user-images.githubusercontent.com/80648379/117587191-c3475580-b0ea-11eb-9f84-616364a7b9b8.png)

* County Results:

    ![Screen Shot 2021-05-09 at 5 18 42 PM](https://user-images.githubusercontent.com/80648379/117587196-cb9f9080-b0ea-11eb-9924-6e628a881ae0.png)

* County with the most votes:

    ![Screen Shot 2021-05-09 at 5 18 50 PM](https://user-images.githubusercontent.com/80648379/117587182-b6c2fd00-b0ea-11eb-8243-98daa3af849e.png)

* Candidate Results:

    ![Screen Shot 2021-05-09 at 5 18 56 PM](https://user-images.githubusercontent.com/80648379/117587215-dbb77000-b0ea-11eb-9d5a-1034cfa067be.png)

* Winner Summary:

    ![Screen Shot 2021-05-09 at 5 19 02 PM](https://user-images.githubusercontent.com/80648379/117587205-d528f880-b0ea-11eb-877a-2cb5486a125d.png)



## Election-Audit Summary
Although this analysis only looks at the 2018 House of Representatives Race for the 1st District in CO, it can easily be manipulated to run results for more districts and other elections. If we wanted to run this analysis on all of the districts in CO, and assuming our data had another column for each district, we could use the ```groupby``` function to group the results by each district. 

