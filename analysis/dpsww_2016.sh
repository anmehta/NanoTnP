#!/bin/bash

#settings_ele_ttH.py settings_ele_dpsww.py

python tnpEGM_fitter.py settings/settings_ele_dpsww_nano.py --flag dpswwElTight --checkBins
python tnpEGM_fitter.py settings/settings_ele_dpsww_nano.py --flag dpswwElTight --createBins
python tnpEGM_fitter.py settings/settings_ele_dpsww_nano.py --flag dpswwElTight --createHists
python tnpEGM_fitter.py settings/settings_ele_dpsww_nano.py --flag dpswwElTight --doFit
python tnpEGM_fitter.py settings/settings_ele_dpsww_nano.py --flag dpswwElTight --doFit --mcSig --altSig
python tnpEGM_fitter.py settings/settings_ele_dpsww_nano.py --flag dpswwElTight --doFit --altSig
python tnpEGM_fitter.py settings/settings_ele_dpsww_nano.py --flag dpswwElTight --doFit --altBkg
python tnpEGM_fitter.py settings/settings_ele_dpsww_nano.py --flag dpswwElTight --sumUp
