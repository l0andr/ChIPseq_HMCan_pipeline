#!/bin/bash
CONDA_PATH="/local/projects-t3/gaykalova/aloginov/miniconda3_latest/"
# >>> conda initialize >>>
__conda_setup="$('/local/projects-t3/gaykalova/aloginov/miniconda3_latest/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f $CONDA_PATH"/etc/profile.d/conda.sh" ]; then
        . $CONDA_PATH"/etc/profile.d/conda.sh"
    else
        export PATH=$CONDA_PATH"/bin":$PATH
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
echo "Job started on:"`hostname`
echo "Job name is:"$JOB_NAME" Jobid="$JOB_ID
export PATH=$CONDA_PREFIX/bin:$PATH
{exec_job}
