# pla-generator
A automated PLA generator for Layout

### Installation:
<!--TODO -->

### Usage:
<!--TODO -->

### Bugs
* Entering the same pla code in the code list of multiple outputs will result in the creation of duplicate code lines
instead of multiple output connections on one code line.

***
# Input Instructions
## Pre-release (i.e. unversioned) input format
`inputs:left_input,input_2,input_3,right_input`  
`outputs:left_output,output_2,output_3,right_output`  
`left_output:pla_code_1`  
`output_2:pla_code_2`  
`output_3:pla_code_3`  
`right_output:pla_code_4` 

### Notes:
* The ordering of the outputs in the list must match the order in which their corresponding pla codes are listed.
* The specification of a sequence of numerical inputs or outputs can be done as follows: `inputs:0..19` or 
`outputs:39..20`.


## Pre-release (i.e. unversioned) input methods
* Input text file
* Input string as parameter (in progress)

