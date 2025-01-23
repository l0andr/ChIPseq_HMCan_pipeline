#!/bin/bash

echo "Post deploy process started"
echo "Check and ensure HMcan instalation (Not implemented)[TODO]"
echo "Check and ensure LILY instalation (Not implemented)[TODO]"
echo "Setup R libs needed for LILY"
Rcommand=`which Rscript`
echo "Will use following Rscript:"$Rcommand
$Rcommand -e 'if (!require("BiocManager", quietly = TRUE)) {install.packages("BiocManager",repos="http://cran.us.r-project.org")}'
$Rcommand -e 'BiocManager::install(c( "Rhtslib", "SummarizedExperiment", "GenomicRanges", "XML", "GenomeInfoDb", "RCurl", "Rsamtools", "GenomicAlignments","rtracklayer"))'
echo "Post deploy process finished"