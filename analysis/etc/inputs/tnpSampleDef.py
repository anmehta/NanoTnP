from libPython.tnpClassUtils import tnpSample
import os
cwd = os.getcwd()
eosdpsww2016 = '/eos/cms/store/cmst3/group/dpsww/tnp_trees_nano/'
latinov6_16 = '%s/../ntuple/results/latinov6_16/' % cwd
latinov6_17 = '%s/../ntuple/results/latinov6_17/' % cwd
latinov6_18 = '%s/../ntuple/results/latinov6_18/' % cwd

latinov7_16 = '%s/../skim/results/latinov7_16/'   % cwd 
latinov7_17 = '%s/../skim/results/latinov7_17/'   % cwd
latinov7_18 = '%s/../skim/results/latinov7_18/'   % cwd

nanoV7_16 = '%s/../skim/results/Full2016v7_102X/' % cwd
nanoV7_17 = '%s/../skim/results/Full2017v7_102X/' % cwd
nanoV7_18 = '%s/../skim/results/Full2018v7_102X/' % cwd




dpsww2016 = {

    'DY_madgraph' : tnpSample('DY_madgraph', 
                                        eosdpsww2016 + 'DYJetsToLL_M50_LO.root',
                                        isMC = True, nEvts =  -1 ),
    'DY_amcatnlo' : tnpSample('DY_amcatnlo', 
                                        eosdpsww2016 + 'DYJetsToLL_M50.root',
                                        isMC = True, nEvts =  -1 ),
#    'data_Run2016' : tnpSample('data_Run2016' , eosdpsww2016 + 'SingleElectron_Run2016.root' , lumi = 35.9 ),
    'data_Run2016' : tnpSample('data_Run2016' , eosdpsww2016 + 'SingleElectron_Run2016B_02Apr2020.root' , lumi = 5.750 ),
##   'data_Run2016B' : tnpSample('data_Run2016B' , eosdpsww2016 + 'SingleElectron_Run2016B_02Apr2020.root' , lumi = 5.750 ),
##   'data_Run2016C' : tnpSample('data_Run2016C' , eosdpsww2016 + 'SingleElectron_Run2016C_02Apr2020.root' , lumi = 2.573 ),
##   'data_Run2016D' : tnpSample('data_Run2016D' , eosdpsww2016 + 'SingleElectron_Run2016D_02Apr2020.root' , lumi = 4.242 ),
##   'data_Run2016E' : tnpSample('data_Run2016E' , eosdpsww2016 + 'SingleElectron_Run2016E_02Apr2020.root' , lumi = 4.422 ),
##   'data_Run2016F' : tnpSample('data_Run2016F' , eosdpsww2016 + 'SingleElectron_Run2016F_02Apr2020.root' , lumi = 3.283 ),
##   'data_Run2016G' : tnpSample('data_Run2016G' , eosdpsww2016 + 'SingleElectron_Run2016G_02Apr2020.root' , lumi = 7.562 ),
##   'data_Run2016H' : tnpSample('data_Run2016H' , eosdpsww2016 + 'SingleElectron_Run2016H_02Apr2020.root' , lumi = 8.979 ),



}

nanov5_16 = {
    'DYJetsToLL_M-50-LO_ext2' : tnpSample('DYJetsToLL_M-50-LO_ext2',
                                     latinov6_16 + 'DYJetsToLL_M-50-LO_ext2.root',
                                     isMC = True, nEvts =  -1 ),

    'DYJetsToLL_M-50' : tnpSample('DYJetsToLL_M-50',
                                  latinov6_16 + 'DYJetsToLL_M-50.root',
                                  isMC = True, nEvts =  -1 ),

    'data_Run2016' : tnpSample('SingleElectron' , latinov6_16 + 'SingleElectron_Run2016.root' , lumi = 35.867 ),
}

nanov5_17 = {
    'DYJetsToLL_M-50-LO_ext1' : tnpSample('DYJetsToLL_M-50-LO_ext1',
                                          latinov6_17 + 'DYJetsToLL_M-50-LO_ext1.root',
                                     isMC = True, nEvts =  -1 ),
    
    'DYJetsToLL_M-50_ext1' : tnpSample('DYJetsToLL_M-50_ext1',
                                       latinov6_17 + 'DYJetsToLL_M-50_ext1.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2017' : tnpSample('SingleElectron' , latinov6_17 + 'SingleElectron_Run2017.root' , lumi = 41.53 ),
}

nanov6_18 = {
    'DYJetsToLL_M-50-LO' : tnpSample('DYJetsToLL_M-50-LO',
                                     latinov6_18 + 'DYJetsToLL_M-50-LO.root',
                                     isMC = True, nEvts =  -1 ),

    'DYJetsToLL_M-50_ext2' : tnpSample('DYJetsToLL_M-50_ext2',
                                      latinov6_18 + 'DYJetsToLL_M-50_ext2.root',
                                      isMC = True, nEvts =  -1 ),

    'data_Run2018' : tnpSample('EGamma' , latinov6_18 + 'EGamma_Run2018.root' , lumi = 59.74 ),

}

#####################
nanov6_16 = {
    'DYJetsToLL_M-50-LO' : tnpSample('DYJetsToLL_M-50-LO_ext1',
                                     latinov7_16 + 'DYJetsToLL_M-50-LO_ext1.root',
                                     isMC = True, nEvts =  -1 ),

    'DYJetsToLL_M-50' : tnpSample('DYJetsToLL_M-50_ext2',
                                  latinov7_16 + 'DYJetsToLL_M-50_ext2.root',
                                  isMC = True, nEvts =  -1 ),

    'data_Run2016' : tnpSample('SingleElectron' , latinov7_16 + 'SingleElectron_Run2016.root' , lumi = 35.867 ),
}

nanov6_17 = {
    'DYJetsToLL_M-50-LO' : tnpSample('DYJetsToLL_M-50-LO_ext1',
                                          latinov7_17 + 'DYJetsToLL_M-50-LO_ext1.root',
                                     isMC = True, nEvts =  -1 ),

    'DYJetsToLL_M-50' : tnpSample('DYJetsToLL_M-50_ext1',
                                       latinov7_17 + 'DYJetsToLL_M-50_ext1.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2017' : tnpSample('SingleElectron' , latinov7_17 + 'SingleElectron_Run2017.root' , lumi = 41.53 ),
    
    'data_Run2017B' : tnpSample('data_Run2017B' , latinov7_17 + 'RunB.root' , lumi = 4.793 ),
    'data_Run2017C' : tnpSample('data_Run2017C' , latinov7_17 + 'RunC.root' , lumi = 9.753),
    'data_Run2017D' : tnpSample('data_Run2017D' , latinov7_17 + 'RunD.root' , lumi = 4.320 ),
    'data_Run2017CD' : tnpSample('data_Run2017CD' , latinov7_17 + 'RunCD.root' , lumi = 14.073 ),
    'data_Run2017E' : tnpSample('data_Run2017E' , latinov7_17 + 'RunE.root' , lumi = 8.802),
    'data_Run2017F' : tnpSample('data_Run2017F' , latinov7_17 + 'RunF.root' , lumi = 13.567),

}

nanov6_1_18 = {
    'DYJetsToLL_M-50-LO' : tnpSample('DYJetsToLL_M-50-LO',
                                     latinov7_18 + 'DYJetsToLL_M-50-LO.root',
                                     isMC = True, nEvts =  -1 ),

    'DYJetsToLL_M-50' : tnpSample('DYJetsToLL_M-50_ext2',
                                      latinov7_18 + 'DYJetsToLL_M-50_ext2.root',
                                      isMC = True, nEvts =  -1 ),

    'data_Run2018' : tnpSample('EGamma' , latinov7_18 + 'EGamma_Run2018.root' , lumi = 59.74 ),

}

##########################
nanov7_16 = {
    'DYJetsToLL_M-50-LO' : tnpSample('DYJetsToLL_M-50-LO_ext1',
                                     nanoV7_16 + 'DYJetsToLL_M-50-LO_ext1.root',
                                     isMC = True, nEvts =  -1 ),

    'DYJetsToLL_M-50' : tnpSample('DYJetsToLL_M-50_ext2',
                                  nanoV7_16 + 'DYJetsToLL_M-50_ext2.root',
                                  isMC = True, nEvts =  -1 ),

    'data_Run2016' : tnpSample('SingleElectron' , nanoV7_16 + 'SingleElectron.root' , lumi = 35.867 ),
}

nanov7_17 = {
    'DYJetsToLL_M-50-LO' : tnpSample('DYJetsToLL_M-50-LO_ext1',
                                          nanoV7_17 + 'DYJetsToLL_M-50-LO_ext1.root',
                                     isMC = True, nEvts =  -1 ),

    'DYJetsToLL_M-50' : tnpSample('DYJetsToLL_M-50_ext1',
                                       nanoV7_17 + 'DYJetsToLL_M-50_ext1.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2017' : tnpSample('SingleElectron' , nanoV7_17 + 'SingleElectron.root' , lumi = 41.53 ),

    'data_Run2017B' : tnpSample('data_Run2017B' , nanoV7_17 + 'SingleElectron_RunB.root' , lumi = 4.793 ),
    'data_Run2017C' : tnpSample('data_Run2017C' , nanoV7_17 + 'SingleElectron_RunC.root' , lumi = 9.753),
    'data_Run2017D' : tnpSample('data_Run2017D' , nanoV7_17 + 'SingleElectron_RunD.root' , lumi = 4.320 ),
    'data_Run2017CD' : tnpSample('data_Run2017CD' , nanoV7_17 + 'SingleElectron_RunCD.root' , lumi = 14.073 ),
    'data_Run2017E' : tnpSample('data_Run2017E' , nanoV7_17 + 'SingleElectron_RunE.root' , lumi = 8.802),
    'data_Run2017F' : tnpSample('data_Run2017F' , nanoV7_17 + 'SingleElectron_RunF.root' , lumi = 13.567),

}

nanov7_18 = {
    'DYJetsToLL_M-50-LO' : tnpSample('DYJetsToLL_M-50-LO',
                                     nanoV7_18 + 'DYJetsToLL_M-50-LO.root',
                                     isMC = True, nEvts =  -1 ),

    'DYJetsToLL_M-50' : tnpSample('DYJetsToLL_M-50_ext2',
                                      nanoV7_18 + 'DYJetsToLL_M-50_ext2.root',
                                      isMC = True, nEvts =  -1 ),

    'data_Run2018' : tnpSample('EGamma' , nanoV7_18 + 'EGamma.root' , lumi = 59.74 ),

}



