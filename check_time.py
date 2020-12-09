import json
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--disablePatatrack', dest='disablePatatrack', default=False, help='disable Patatrack in the running')
parser.add_argument('--disableFacile',    dest='disableFacile',    default=False, help='disable Facile in the running')
parser.add_argument('--PatatrackCPU',     dest='PatatrackCPU',     default=False, help='run Patatrack recipe with the CPU')
parser.add_argument('--HCALGPU',          dest='HCALGPU',          default=False, help='run HCAL GPU reco')

opt = parser.parse_args()

if opt.disablePatatrack and opt.PatatrackCPU:
    print("Patatrack module disabled. No CPU running either")
    opt.PatatrackCPU = 0

if not opt.disableFacile and opt.HCALGPU:
    print("Facile enabled. NO HCAL MAHI GPU reconstruction")
    opt.HCALGPU = 0

jsonName = "resources_woPatatrack" if opt.disablePatatrack else "resources_Patatrack"
jsonName += "CPU" if opt.PatatrackCPU else ""
jsonName += "_woFacile" if opt.disableFacile else "_Facile"
jsonName += "_HCALGPU" if opt.HCALGPU else ""
jsonName += ".json"

#timeName = "time_thread"
timeName = "time_real"


f = open(jsonName)
data = json.load(f)

nevents = data["total"]["events"] 
time_total = data["total"][timeName]

time_real_modules = {}

## convert json to easy-to-use map
for i in xrange(len(data['modules'])):
    module = data['modules'][i]
    time_real_modules[module["label"]] = module[timeName]


def Modules_for_Patatrack_or_Equivalent(with_patatrack=True):
    ## Patatrack part
    # CPU GPU status
    # from https://github.com/cms-sw/cmssw/blob/CMSSW_11_2_Patatrack_X/HLTrigger/Configuration/python/customizeHLTforPatatrack.py#L45-L61
    # these times are usually pretty small to be negligible
    status = [
        "statusOnGPU",
        "statusOnGPU@cpu",
        "statusOnGPU@cuda",
        "statusOnGPUFilter",
        "Status_OnGPU",
    ]

    # pixel local reconstruction
    # from https://github.com/cms-sw/cmssw/blob/CMSSW_11_2_Patatrack_X/HLTrigger/Configuration/python/customizeHLTforPatatrack.py#L202-L213
    localpixel = [ 
        "hltOnlineBeamSpotToCUDA", # GPU
        "hltSiPixelClustersCUDA",  # GPU
        "hltSiPixelRecHitsCUDA",   # GPU
        "hltSiPixelDigisSoA",      # GPU
        "hltSiPixelDigisClusters", # GPU
        "hltSiPixelDigiErrorsSoA", # GPU
        "hltSiPixelDigiErrors",    # GPU
        "hltSiPixelDigis",         # GPU
        "hltSiPixelDigis@cpu",     # CPU
        "hltSiPixelClusters",      # CPU and GPU
        "hltSiPixelClustersCache", # CPU and GPU
        "hltSiPixelRecHits@cuda",  # GPU
        "hltSiPixelRecHits@cpu",   # CPU
    ]
    
    # pixel track reconstruction
    # from https://github.com/cms-sw/cmssw/blob/CMSSW_11_2_Patatrack_X/HLTrigger/Configuration/python/customizeHLTforPatatrack.py#L315-L320
    recopixeltracks = [
        "hltPixelTracksTrackingRegions",
        "hltSiPixelRecHitSoA",            # CPU
        "hltPixelTracksCUDA",             # GPU
        "hltPixelTracksSoA@cuda",         # GPU
        "hltPixelTracksSoA@cpu",          # CPU
        "hltPixelTracks",                 # CPU and GPU
    ]

    # pixel vertex reconstruction
    # from https://github.com/cms-sw/cmssw/blob/CMSSW_11_2_Patatrack_X/HLTrigger/Configuration/python/customizeHLTforPatatrack.py#L325-L335
    recopixelvertexing = [
        "hltPixelTracksFitter",      # CPU and GPU
        "hltPixelTracksFilter",      # CPU and GPU
        "hltPixelVerticesCUDA",      # GPU
        "hltPixelVerticesSoA@cuda",  # GPU
        "hltPixelVerticesSoA@cpu",   # CPU
        "hltPixelVertices",          # CPU and GPU
        "hltTrimmedPixelVertices",   # CPU and GPU
    ]

    modules_patatrack = status + localpixel + recopixeltracks + recopixelvertexing

    # Standard pixel reconstruction, no patatrack involved
    # HLTDoLocalPixelSequence
    # from https://github.com/cms-sw/cmssw/blob/CMSSW_11_2_Patatrack_X/HLTrigger/Configuration/python/HLT_GRun_cff.py
    localpixel_standard = [
        "hltSiPixelDigis",
        "hltSiPixelClusters",
        "hltSiPixelClustersCache",
        "hltSiPixelRecHits",
    ]
    
    recopixeltracks_standard = [
        "hltPixelTracksFilter",
        "hltPixelTracksFitter",
        "hltPixelTracksTrackingRegions",
        "hltPixelLayerQuadruplets",
        "hltPixelTracksHitDoublets",
        "hltPixelTracksHitQuadruplets",
        "hltPixelTracks",
    ]
    
    recopixelvertexing_standard = [
        "hltPixelVertices",
        "hltTrimmedPixelVertices",
    ]

    modules_patatrack_equivalent = localpixel_standard + recopixeltracks_standard + recopixelvertexing_standard

    if with_patatrack:
        return modules_patatrack
    else:
        return modules_patatrack_equivalent

def Modules_for_FACILE_or_Equivalent(with_facile=True, with_HCALGPU=False):
    ## FACILE
    hltHbhereco = [
        "hltHbherecopre",
        "hltHbhereco",
    ]
    hltHbhereco_hcalgpu = [
        "hltHcalDigisGPU",
        "hltHbherecoGPU",
        "hltHbherecoFromGPU",
        "hltHbhereco",
    ]
    hltHbhereco_nofacile = [
        "hltHbhereco"
    ]

    if with_facile:
        return hltHbhereco
    elif with_HCALGPU:
        return hltHbhereco_hcalgpu
    else:
        return hltHbhereco_nofacile


withPatatrack = not opt.disablePatatrack
withFacile   = not opt.disableFacile
withHCALGPU = opt.HCALGPU

time_patatrack = sum(time_real_modules[mod] for mod in Modules_for_Patatrack_or_Equivalent(withPatatrack))
time_facile = sum(time_real_modules[mod] for mod in Modules_for_FACILE_or_Equivalent(withFacile, withHCALGPU))

time_other = time_real_modules["other"]  

time_HLT = time_total - time_other

print("Json file:\t%s"       %jsonName)
print("Total time:\t%.2f"    %(time_total/nevents    ))
print("Other time:\t%.2f"    %(time_other/nevents    ))
print("HLT time:\t%.2f"      %(time_HLT/nevents      ))
print("Patatrack time:\t%.2f"%(time_patatrack/nevents))
print("facile time:\t%.2f"   %(time_facile/nevents   ))
