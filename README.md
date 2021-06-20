# pip freeze requirement cleaner

Clean the `requirments.txt` generated from `pip freeze` which contains something like this:

```shell
absl-py==0.12.0
appnope @ file:///opt/concourse/worker/volumes/live/4f734db2-9ca8-4d8b-5b29-6ca15b4b4772/volume/appnope_1606859466979/work
argon2-cffi @ file:///opt/concourse/worker/volumes/live/4afd07c8-7fc3-4a09-6326-d8c70269eb33/volume/argon2-cffi_1613037490059/work
astor==0.8.1
astunparse==1.6.3
async-generator==1.10
attrs @ file:///tmp/build/80754af9/attrs_1604765588209/work
backcall @ file:///home/ktietz/src/ci/backcall_1611930011877/work
bleach @ file:///tmp/build/80754af9/bleach_1612211392645/work
cachetools==4.2.1
certifi==2020.12.5
```

This code helps to clean your requirements file.

#### Run Instructions

```shell
git clone git@github.com:rancheng/pip_freeze_cleaner.git
cd pip_freeze_cleaner
python clean_requirements.py /path/to/your/requirements.txt
```

It will create a file with `_fixed.txt` suffix at the same folder of the input requirements file.