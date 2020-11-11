#############################################################
########## General settings
#############################################################
# flag to be Tested
deno_sel = '(TnP_trigger && Tag_pt > 37 && abs(Tag_eta) < 2.5 && Tag_jetRelIso < 0.15 && Probe_charge*Tag_charge < 0 && abs(Tag_dxy) < 0.05 && abs(Tag_dz) < 0.1 && Tag_isGenMatched == 1 && Probe_isGenMatched == 1 && Probe_pt > 7 && abs(Probe_eta) < 2.5 && abs(Probe_dxy)<0.05 && abs(Probe_dz)<0.1 && Probe_miniPFRelIso_all < 0.4 && Probe_sip3d < 8  && Probe_mvaFall17V2noIso_WPL && TnP_mass > 60 && TnP_mass <= 120)'
dpswwElTight = '{deno} && (Probe_pt > 10 && (Probe_hoe<(0.10-0.00*(abs((Probe_deltaEtaSC) - (-Probe_eta))>1.479))) && (Probe_eInvMinusPInv>-0.04)&& (Probe_sieie<(0.011-(-0.019)*(abs((Probe_deltaEtaSC)-(-Probe_eta))>1.479))) && Probe_convVeto &&  Probe_jetBTagDeepFlavB < 0.3093 && Probe_lostHits == 0 && Probe_mvaTTH > 0.7 && Probe_tightCharge>=2)'.format(deno=deno_sel)


# flag to be Tested
flags = {
    'dpswwElTight' : dpswwElTight,
    }

baseOutDir = 'results/dpsww2016withNANOInf/tnpEleID/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'Events'
samplesDef = {
    'data'   : tnpSamples.dpsww2016['data_Run2016'].clone(),
    'mcNom'  : tnpSamples.dpsww2016['DY_madgraph'].clone(),
    'mcAlt'  : tnpSamples.dpsww2016['DY_amcatnlo'].clone(),
    'tagSel' : tnpSamples.dpsww2016['DY_madgraph'].clone(),
}

## can add data sample easily
##samplesDef['data'].add_sample( tnpSamples.dpsww2016['data_Run2016C'] )
##samplesDef['data'].add_sample( tnpSamples.dpsww2016['data_Run2016D'] )
##samplesDef['data'].add_sample( tnpSamples.dpsww2016['data_Run2016E'] )
##samplesDef['data'].add_sample( tnpSamples.dpsww2016['data_Run2016F'] )
##samplesDef['data'].add_sample( tnpSamples.dpsww2016['data_Run2016G'] )
##samplesDef['data'].add_sample( tnpSamples.dpsww2016['data_Run2016H'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
    samplesDef['tagSel'].set_cut('Tag_pt > 37 && abs(Tag_eta) < 2.5 && Tag_jetRelIso < 0.15 && abs(Tag_dxy) < 0.05 && abs(Tag_dz) < 0.1 && Tag_isGenMatched == 1')

## set MC weight, simple way (use tree weight) 
weightName = 'puWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)



#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
    { 'var' : 'Probe_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
    #{ 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.1,-1.2,-0.9,0.0,0.9,1.2,2.1,2.5] },
    #{ 'var' : 'Probe_eta' , 'type': 'float', 'bins': [0.0,0.9,1.2,2.1,2.5] },
    #{ 'var' : 'Probe_pt' , 'type': 'float', 'bins': [10,15,20,25,30,35,40,45,60,80,120] },
    { 'var' : 'Probe_pt' , 'type': 'float', 'bins': [10,20,35,50,100,200,500]}
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut


cutBase   = deno_sel

#'tag_Ele_pt > 35 && el_q*tag_Ele_q < 0 && el_ptAM > 7 && abs(el_eta) < 2.5 &&  !(1.4442 < abs(el_eta) < 1.566) && abs(el_dxy) < 0.05 && abs(el_dz) < 0.1 && el_sip3dAM < 8 && el_mHits <=1 && el_miniIsoAllAM < 0.4 && passingMVA94XwpLoosenoisoV2 && abs(tag_Ele_eta) < 2.5 && abs(tag_Ele_dxy) < 0.05 && abs(tag_Ele_dz) < 0.1'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
##amadditionalCuts = { 
##am    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
##am    1 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
##am    2 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
##am    3 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
##am    4 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
##am    5 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
##am    6 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
##am    7 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
##am    8 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
##am    9 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
##am}

#### or remove any additional cut (default) (tried this one, no effect)
##amadditionalCuts = { 
##am    0 : 'tag_Ele_trigMVA > 0.92 ',
##am    1 : 'tag_Ele_trigMVA > 0.92 ',
##am    2 : 'tag_Ele_trigMVA > 0.92 ',
##am    3 : 'tag_Ele_trigMVA > 0.92 ',
##am    4 : 'tag_Ele_trigMVA > 0.92 ',
##am    5 : 'tag_Ele_trigMVA > 0.92 ',
##am    6 : 'tag_Ele_trigMVA > 0.92 ',
##am    7 : 'tag_Ele_trigMVA > 0.92 ',
##am    8 : 'tag_Ele_trigMVA > 0.92 ',
##am    9 : 'tag_Ele_trigMVA > 0.92 '
##am}

additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]

tnpParAltSigFit_addGaus = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,6.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "meanGF[80.0,70.0,100.0]","sigmaGF[15,5.0,125.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,85.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
         
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]

##amnpParNomFit = [
##am   "meanP[-0.0,-5.0,5.0]","sigmaP[2.5,0.065,3.0]",
##am   "meanF[-0.0,-5.0,5.0]","sigmaF[0.5,0.0,1.0]",
##am   "acmsP[60.,45.,80.]","betaP[0.05,-1.0,1.0]","gammaP[0.1, -2, 2]","peakP[90.0]",
##am   "acmsF[60.,50.,80.]","betaF[0.0,-1,1.0]","gammaF[0.1, -2, 2]","peakF[90.0]",

##am    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
##am    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
##am    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
##am    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

##am    "meanP[0.5,0,5.0]","sigmaP[2.5,1.5,3.0]",
##am    "meanF[0.5,0,1.0]","sigmaF[0.5,0.0,2.5]",
##am    "acmsP[50.,45.,70.]","betaP[0.05,-1.0,1.0]","gammaP[0.1, -2, 2]","peakP[90.0]",
##am    "acmsF[70.,50.,120.]","betaF[0.0,-1,1.0]","gammaF[0.1, -2, 2]","peakF[90.0]",
##am    "meanP[-0.20,-5.0,0.65]","sigmaP[0.05,0.055,1.0]", 
##am    "meanF[-0.2,-5.0,0.65]","sigmaF[0.05,0.065,1.0]",
##am    "acmsP[70,50,120.]","betaP[0.0,-1,1]","gammaP[0.2, 0.005, 1]","peakP[90.0]",
##am    "acmsF[70,50,120.]","betaF[0.0,-1,1]","gammaF[0.2, 0.005, 1]","peakF[90.0]",
##am    ]
##am
##amtnpParAltSigFit = [
##am    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
##am    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
##am    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
##am    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
##am    ]
##am     
##amtnpParAltBkgFit = [
##am    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
##am    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
##am    "alphaP[0.,-5.,5.]",
##am    "alphaF[0.,-5.,5.]",
##am    ]
        



##am bin 8    "meanP[-0.0,-5.0,5.0]","sigmaP[2.5,0.065,3.0]",
##am bin 8    "meanF[-0.0,-5.0,5.0]","sigmaF[2.5,0.065,3.0]",
##am bin 8    "acmsP[20.,45.,60.]","betaP[0.05,-1.0,1.0]","gammaP[0.1, -2, 2]","peakP[90.0]",
##am bin 8    "acmsF[20.,45.,60.]","betaF[0.0,-1,1.0]","gammaF[0.1, -2, 2]","peakF[90.0]",
