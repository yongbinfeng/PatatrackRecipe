# steps to run Patatrack and FACILE on the same GPU
```
cmsrel CMSSW_11_2_0_pre10_Patatrack
cd CMSSW_11_2_0_pre10_Patatrack/src/
cmsenv
# merge the FACILE branch
git cms-merge-topic yongbinfeng:hcalreco-facile-squash
```
This branch is rebased from `jeffkrupa:hcalreco-facile-squash`, to make it compatible with `CMSSW_11_2_0_pre10_Patatrack`. 

Then add the FACILE data files:
```
git cms-addpkg HeterogeneousCore/SonicTriton
git clone https://github.com/hls-fpga-machine-learning/sonic-models HeterogeneousCore/SonicTriton/data
scram b -j 10
```

Run the `test_conf.py` under `$CMSSW_BASE/src`. The Patatrack and FACILE can be disabled by `disablePatatrack=1` and `disableFacile=1` respectively. To run Patatrack on CPU, do `cmsRun test_conf.py PatatrackCPU=1`.

The script will produce the json files documenting the HLT timing information using the [`FastTimerService`](https://github.com/cms-sw/cmssw/blob/CMSSW_11_2_Patatrack_X/HLTrigger/Timer/plugins/FastTimerService.cc). The json file can be analyzed with `check_time.py` by running:
```
python check_time.py --disablePatatrack 1 --disableFacile 1
```
or similar
