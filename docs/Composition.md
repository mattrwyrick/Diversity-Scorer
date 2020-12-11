# Composition

## About
This is a json formatted file where a user can enter in a distribution to reuse for organization generator and scoring. 
The user enters in whole number amounts per demographic and the tool will calculate the percentages later as it builds 
and scores

## Format
Compositions should be json files that contain a list of dictionaries. Each dictionary must contain a keyword "amount" 
and then it will contain any other key-value pairs to describe the desired demographics.
```
[ 
   {   
      "amount": <int>,
      "my key1": <any>,
      "e.g. gender": <str>,
      "e.g. ethnicity": <str>, 
      "e.g. income level": <int>,
   },
   
                .
                .
                .
   
   
   {
        same keywords expected for all dictionaries
   }
]

```