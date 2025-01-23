## Calling Super-enchancers using HMCan and LILY pipeline (version 0.5)

### Usage:

1. Edit config.yaml and setup pathes to input and output directories
```yaml
input_dir: "/input/raw_data/something/funny"
file_mask: "*.bam"
use_subdirs: True
output_dir: "/output/something/again/funny/hmcan"
```

Set <b>use_subdirs</b> to True, if you need files from sub-directories too

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
git commit -a -m "Fix FastQC vonfig fro project blabla. Or some another message"
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
