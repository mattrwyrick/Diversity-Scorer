# Diver(S)tudio
Application and Toolkit for creating and measuring diversity amongst organizations

## Setup
`pip install -r requirements.txt`  

## Data
This application works by generating tree structured organizations. Seeds can be created that have a probabilistic range 
of depths and breadths that tell a node how many children it will have, and how long the seed should persist down the 
as the structure builds. Each seed also contains an attribute generator for the node that represents a probabilistic 
demographic the node (or employee) will have. Each seed contains a random stop percentage that checks before each node 
gets created. A seed will either stop at its specified depth or earlier if the random stop percentage triggers. When a 
seed stops it will then switch over to a another seed. It will select from a probabilistic set of seeds it has specified
it can switch over too. The next seed can also have another set of seeds to select and switch over to when it 
terminates. When the set of seeds is finally empty, a leaf node (or employee that manages no one) has been reached.

## Scoring
TODO  
SimpleScore evaluates diff in %'s from actual vs target distribution at the ceo level of an organization (divided by 2)  

## Results
* Random seed set to 1234567890   
* 1 run through per organization  
* max depth of 8 for the tree   
* breadth varies (20%-2, 40%-3, %40-4)
* read scores as: (score) (org type)

### Uniform All Target

#### Simple Score
0.00478183081 uniform   
0.17057010785 male 2x   
0.16627497062 female 2x   
0.25313059033 male 3x   
0.25134236021 female 3x  

#### Simple Chi Square (p value)
1.0 uniform  
0.73478 male 2x  
0.76535 female 2x  
0.13089 male 3x  
0.14165 female 3x  

### 2x Female - Uniform Ethnicity Target

#### Simple Score
0.16655577077 uniform   
0.33723677452 male 2x   
0.01585063324 female 2x   
0.41979725700 male 3x   
0.08467569355 female 3x  

#### Simple Chi Square 
0.76825 uniform  
0.00667 male 2x  
1.0 female 2x  
5e-05 male 3x  
0.99493 female 3x  

### 2x Male - Uniform Ethnicity Target

#### Simple Score
0.16677756255 uniform   
0.01463790446 male 2x   
0.33294163728 female 2x   
0.08646392367 male 3x   
0.41800902688 female 3x 

#### Simple Chi Square  
0.76685 uniform  
1.0 male 2x  
0.00822 female 2x  
0.99302 male 3x  
5e-05 female 3x  

## Usage

* Create demographic compositions under `/src/diverstudio/presets/compositions/*`
* Create organizations in `/src/diverstudio/presets/generic_seeds.py`
* Create targets in `/src/diverstudio/presets/generic_targets.py`
* Interact (generation + score) in `/src/diverstudio/presets/generic_interact.py`  
* Run the application from `/src/diverstudio/main.py`  


