## Multi BAM QC Snakemake pipeline (version 0.5)

This pipeline compute different QC metrics for multiple bam files with results of ChIP-seq experiments.
It uses qualimap, plotFingerprint and bamCoverage tools.

### Usage:

1. Edit config.yaml and setup pathes to input and output directories
```yaml
input_dir: "/local/input_dir"
file_mask: "*.bam"
use_subdirs: False
output_dir: "/local/output_dir"
tmp_dir: "/local/tmp_dir/"

qulimap_threads: 15
mem_size_in_gb: 25

#following samples labels expected on the start of bam files names
list_of_samples: ['OKF6','30694N','30694T','30709N','30709T','30866N','30866T']

run_qualimap_multi_bam: True
qualimap_multi_bam_labels_file: ""
qualimap_multi_bam_reports_dir: ""

run_plotFingerprint: True
plotFingerprint_dir: ""
fingerPrintParams: "--smartLabels --minMappingQuality 30 --skipZeros"

run_bamCoverage: True
bamCoverage_dir: ""
bamCoverageParams: "--binSize 100 --normalizeUsing RPGC --effectiveGenomeSize 2913022398 --extendReads --ignoreDuplicates"
```
<b> input_dir </b> - Directory with input fastq files <br>
<b> file_mask </b> - Used file mask  <br>
Set <b>use_subdirs</b> to True, if you need files from sub-directories too <br>
<b> number_of_threads_mapper, number_of_threads_samtools </b> - number of threads used in bva-mem2 and samtools <br> 
<b> output_dir </b> - overall output diretory where reports and other files will be created <br>
<b> tmp_dir </b> - working directory for jobs <br>
<b> list_of_samples </b> - list of samples labels expected on the start of bam files names <br>
<b> run_qualimap_multi_bam </b> - switch on rule for run qualimap multi bam <br>
<b> qualimap_multi_bam_labels_file </b> - file with labels for qualimap multi bam [Optional]<br>
<b> qualimap_multi_bam_reports_dir </b> - output diretory for qualimap multi bam reports [Optional]<br>
<b> run_plotFingerprint </b> - switch on rule for run plotFingerprint <br>
<b> plotFingerprint_dir </b> - output diretory for plotFingerprint reports [Optional]<br>
<b> fingerPrintParams </b> - parameters for plotFingerprint <br>
<b> run_bamCoverage </b> - switch on rule for run bamCoverage <br>
<b> bamCoverage_dir </b> - output diretory for bamCoverage reports [Optional]<br>
<b> bamCoverageParams </b> - parameters for bamCoverage <br>



#### <i>Tip:</i>
<details>

<summary> <i> It's good practice to create your own Git branch before making any changes. Read more...</i></summary>

It's good practice to create your own Git branch before making any changes.
So, in the directory where you cloned 'goodnuff', execute the following commands:

```
git checkout master
git pull
```

It will download last version of master or dev branch to your system.
Then, create your own branch:

```
git checkout -b project/your_project_name_or_something_else
```

Now, you are in your branch, and you can make any fixes you want, which will be stored only in your branch.

For example, edit any config files.

Then you can execute following:

```commandline
git commit -a -m "Fix FastQC config fro project blabla. Or some another message"
```

And save your changes in your local git repository


Then, if you would like to share this changes you can also perform

```commandline
git push -u origin <your_branch_name>
```

All changes will be saved in remote repository too. But stored in your separate branch

</details>
2. Local run:

```commandline
snakemake --use-conda --cores 4 
```
