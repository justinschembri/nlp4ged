# Data Storage Overview

Data used in this work is divided into inputs and outputs. Files located in the 
root directory are specific to the publication [link pending]. 

## Output Directory

The file *'sample_2_classified_and_clustered.xlsx'* is the output of the 
classification and clustering steps as deployed on the 
'sample_2_unclassified' file in the input folder. Used to build regex.

The file *'complete_with_ged_conclusions.csv'* is the output of the entire pipeline, as above and including the deployment of regex and logical passes.

These files are manually placed at the root directory. Any other outputs that are generated are placed in dated folders.

### Dated Directories 

If the main script is re-run, newly generated data will be placed in dated and
numbered directories inside the output directory.

## Input Directory

Below an explanation of file contents:

- *complete_unclassified.xlsx* : The full dataset specific to this work. Generally, for use with the complete pipeline (classify, cluster, regex and logic). The main.py script points to this file.

- *sample_1_classified* : The learning dataset for the classifier. The classifier scripts point to this dataset.

- *sample_2_unclassified* : A subset of the full dataset with no overlap with sample 1. Classified and clustered, the outputs (see: sample_2_classified_and_clustered in the output folder) are used to build regex. The main.py scripts point to this dataset.