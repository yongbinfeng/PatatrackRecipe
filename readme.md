```
cmsrel CMSSW_11_2_3_Patatrack
cd CMSSW_11_2_3_Patatrack/src/
cmsenv
scram b -j 10
```

Run the `test_conf.py` under `$CMSSW_BASE/src`. The Patatrack and MAHI GPU can be disabled by `disablePatatrack=1` and `disableFacile=1` respectively. To run Patatrack on CPU, do `cmsRun test_conf.py PatatrackCPU=1`.

The script will produce the json files documenting the HLT timing information using the [`FastTimerService`](https://github.com/cms-sw/cmssw/blob/CMSSW_11_2_Patatrack_X/HLTrigger/Timer/plugins/FastTimerService.cc). The json file can be analyzed with `check_time.py` by running:
```
python check_time.py --disablePatatrack 1
```
or similar
