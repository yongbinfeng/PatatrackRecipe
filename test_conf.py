# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --python_filename=test_conf.py --processName=HLTX --hltProcess=HLTX --conditions auto:phase1_2021_realistic -n 30000 --era Run3 --eventcontent FEVTDEBUGHLT -s HLT:@relval2021 --datatier GEN-SIM-DIGI-RAW --geometry DB:Extended --filein /storage/local/data1/relval/CMSSW_11_2_0_pre6_ROOT622/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/112X_mcRun3_2021_realistic_v7-v1/FED4709C-569E-0A42-8FF7-20E565ABE999.root --nThreads=4 --no_output --no_exec --customise_commands=process.options.wantSummary = True
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('HLTX',Run3)

import FWCore.ParameterSet.VarParsing as VarParsing
opt = VarParsing.VarParsing ('analysis')
opt.register('disablePatatrack', 0, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.bool, 'Set to 1 to disable Patatrack')
opt.register('disableFacile',    0, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.bool, 'Set to 1 to disable Facile')
opt.register('PatatrackCPU',     0, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.bool, 'Set to 1 to run Patatrack on CPU')
opt.register('HCALGPU',          0, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.bool, 'Set to 1 to run HCAL GPU reco')
opt.parseArguments()

if opt.disablePatatrack and opt.PatatrackCPU:
    print("Patatrack module disabled. No CPU running either")
    opt.PatatrackCPU = 0

if not opt.disableFacile and opt.HCALGPU:
    print("Facile enabled. NO HCAL MAHI GPU reconstruction")
    opt.HCALGPU = 0

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 10000 )
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/storage/local/data1/relval/CMSSW_11_2_0_pre6_ROOT622/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/112X_mcRun3_2021_realistic_v7-v1/18477778-2F96-A24A-89F8-BAB9D113611C.root',
        'file:/storage/local/data1/relval/CMSSW_11_2_0_pre6_ROOT622/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/112X_mcRun3_2021_realistic_v7-v1/5087AFB6-88B6-3F40-A9B3-D705E0D3B095.root',
        'file:/storage/local/data1/relval/CMSSW_11_2_0_pre6_ROOT622/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/112X_mcRun3_2021_realistic_v7-v1/5E8F91BB-085F-8E4E-869F-65F120E7E7B5.root',
        'file:/storage/local/data1/relval/CMSSW_11_2_0_pre6_ROOT622/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/112X_mcRun3_2021_realistic_v7-v1/5EC19BD5-CD0C-EB48-AF3D-1E25250D167A.root',
        'file:/storage/local/data1/relval/CMSSW_11_2_0_pre6_ROOT622/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/112X_mcRun3_2021_realistic_v7-v1/6F8EDE6D-EE14-044B-8628-08385B6AC103.root',
        'file:/storage/local/data1/relval/CMSSW_11_2_0_pre6_ROOT622/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/112X_mcRun3_2021_realistic_v7-v1/773FAC39-3A0F-1D44-9567-C5837ADA6244.root',
        'file:/storage/local/data1/relval/CMSSW_11_2_0_pre6_ROOT622/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/112X_mcRun3_2021_realistic_v7-v1/AD1F232C-9D23-BC48-BB4B-DF3D73CD5BA3.root',
        'file:/storage/local/data1/relval/CMSSW_11_2_0_pre6_ROOT622/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/112X_mcRun3_2021_realistic_v7-v1/D05C202C-CCFB-584F-AC7F-CA1ED0197B5E.root',
        'file:/storage/local/data1/relval/CMSSW_11_2_0_pre6_ROOT622/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/112X_mcRun3_2021_realistic_v7-v1/FED4709C-569E-0A42-8FF7-20E565ABE999.root',
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:30000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule()
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

## FastTime service
jsonName = "resources_woPatatrack" if opt.disablePatatrack else "resources_Patatrack"
jsonName += "CPU" if opt.PatatrackCPU else ""
jsonName += "_woFacile" if opt.disableFacile else "_Facile"
jsonName += "_HCALGPU" if opt.HCALGPU else ""
jsonName += ".json"
process.FastTimerService = cms.Service( "FastTimerService",
    dqmPath = cms.untracked.string( "HLT/TimerService" ),
    dqmModuleTimeRange = cms.untracked.double( 40.0 ),
    enableDQMbyPath = cms.untracked.bool( False ),
    writeJSONSummary = cms.untracked.bool( True ),
    dqmPathMemoryResolution = cms.untracked.double( 5000.0 ),
    enableDQM = cms.untracked.bool( True ),
    enableDQMbyModule = cms.untracked.bool( False ),
    dqmModuleMemoryRange = cms.untracked.double( 100000.0 ),
    dqmModuleMemoryResolution = cms.untracked.double( 500.0 ),
    dqmMemoryResolution = cms.untracked.double( 5000.0 ),
    enableDQMbyLumiSection = cms.untracked.bool( False ),
    dqmPathTimeResolution = cms.untracked.double( 0.5 ),
    printEventSummary = cms.untracked.bool( False ),
    dqmPathTimeRange = cms.untracked.double( 100.0 ),
    dqmTimeRange = cms.untracked.double( 2000.0 ),
    enableDQMTransitions = cms.untracked.bool( False ),
    dqmPathMemoryRange = cms.untracked.double( 1000000.0 ),
    dqmLumiSectionsRange = cms.untracked.uint32( 2500 ),
    enableDQMbyProcesses = cms.untracked.bool( True ),
    dqmMemoryRange = cms.untracked.double( 1000000.0 ),
    dqmTimeResolution = cms.untracked.double( 5.0 ),
    printRunSummary = cms.untracked.bool( False ),
    dqmModuleTimeResolution = cms.untracked.double( 0.2 ),
    printJobSummary = cms.untracked.bool( True ),
    jsonFileName = cms.untracked.string( jsonName )
)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

## Patatrack
### do not use customizeHLTforPatatrack since it includes the ecal and hcal local reco on GPU
#from HLTrigger.Configuration.customizeHLTforPatatrack import customizeHLTforPatatrack
#process = customizeHLTforPatatrack(process)
if not opt.disablePatatrack:
    print("include Patatrack Reconstruction")
    from HLTrigger.Configuration.customizeHLTforPatatrack import forceGpuOffload, customiseCommon, customisePixelLocalReconstruction, customisePixelTrackReconstruction
    if opt.PatatrackCPU:
        print("Run Patatrack on CPU")
        import os
        # there might be better ways to do this
        os.environ["CUDA_VISIBLE_DEVICES"] = "" 
        # forceGpuOffload will make Patatrack code running on CPU, but 100MB memory on GPU will be reserved by cmsRun
        #forceGpuOffload(False)
    process = customiseCommon(process)
    process = customisePixelLocalReconstruction(process)
    process = customisePixelTrackReconstruction(process)

## FACILE related
if not opt.disableFacile:
    print("include FACILE")
    process.hltHbherecopre = process.hltHbhereco.clone(
        makeRecHits = cms.bool(False),
        saveInfos = cms.bool(True),
    )

    from RecoLocalCalo.HcalRecProducers.facileHcalReconstructor_cfi import sonic_hbheprereco
    process.hltHbhereco = sonic_hbheprereco.clone(
        ChannelInfoName = cms.InputTag("hltHbherecopre")
    )

    process.HLTDoLocalHcalSequence = cms.Sequence( process.hltHcalDigis + process.hltHbherecopre + process.hltHbhereco + process.hltHfprereco + process.hltHfreco + process.hltHoreco )
    process.HLTStoppedHSCPLocalHcalReco = cms.Sequence( process.hltHcalDigis + process.hltHbherecopre + process.hltHbhereco)
    process.hltHbhereco.Client.verbose = False

# HCAL MAHI GPU code
if opt.HCALGPU:
    # opt.disableFacile has to be true (FACILE disabled), then MAHI GPU code can run
    print("include HCAL GPU Reconstruction")
    from HLTrigger.Configuration.customizeHLTforPatatrack import customiseHcalLocalReconstruction

    if 'Status_OnGPU' not in process.__dict__:
        print("import Common config")
        from HLTrigger.Configuration.customizeHLTforPatatrack import customiseCommon
        process = customiseCommon(process)

    process = customiseHcalLocalReconstruction(process)

# End of customisation functions

# log
process.MessageLogger.cerr.FwkReport.reportEvery = 5000
process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
process.MessageLogger.categories.append('L1GtTrigReport')
process.MessageLogger.categories.append('L1TGlobalSummary')
process.MessageLogger.categories.append('HLTrigReport')
process.MessageLogger.categories.append('FastReport')
process.MessageLogger.suppressWarning = cms.untracked.vstring('hltL3NoFiltersNoVtxMuonsOIState', 'hltL3NoFiltersNoVtxMuonsOIHit', 'hltEgammaGsfTracks', 'hltEcalRecHit') 


# Customisation from command line

process.options.wantSummary = True
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
