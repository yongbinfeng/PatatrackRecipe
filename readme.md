# steps to run PataTrack and FACILE on the same GPU
```
cmsrel CMSSW_11_2_0_pre10_Patatrack
cd CMSSW_11_2_0_pre10_Patatrack/src/
cmsenv
# merge the FACILE branch
git cms-merge-topic yongbinfeng:hcalreco-facile-squash
```
This branch is rebased from `jeffkrupa:hcalreco-facile-squash`, to make it compatible with `CMSSW_11_2_0_pre10_Patatrack`. 

Then add the FACILE data files.
```
git cms-addpkg HeterogeneousCore/SonicTriton
git clone https://github.com/hls-fpga-machine-learning/sonic-models HeterogeneousCore/SonicTriton/data
scram b -j 10
```

Run the `test_conf.py` under `$CMSSW_BASE/src`. The Patatrack and FACILE can be disabled by `disablePataTrack=1` and `disableFacile=1` respectively. To run Patatrack on CPU, do `CUDA_VISIBLE_DEVICES= cmsRun test_conf.py` 
