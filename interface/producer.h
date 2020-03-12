#ifndef PRODUCER_H
#define PRODUCER_H
#include "nanotnp.h"

/*
 * EDProducer
 * tagEle
 * https://github.com/cms-analysis/EgammaAnalysis-TnPTreeProducer/blob/master/python/egmTreesSetup_cff.py#L29-L37
 * 1.) fulfill tightcutbased
 * 2.) match to last filter
 */
 template<typename T>
 auto tagCandProducer(T &df) {
  //https://github.com/cms-analysis/EgammaAnalysis-TnPTreeProducer/blob/master/python/egmElectronIDModules_cff.py#L144-L150
  return df.Define("tagCand","Electron_cutBased>3 && Electron_pt>=30 && abs(Electron_eta)<= 2.1 && !(abs(Electron_eta)>= 1.4442 && abs(Electron_eta)<=1.566)"); // tag cuts
}

/*
 * Matching producer
 * trg-matching: https://github.com/cms-analysis/EgammaAnalysis-TnPTreeProducer/blob/master/python/egmTreesSetup_cff.py#L30-L37
 * gen-matching: https://github.com/cms-analysis/EgammaAnalysis-TnPTreeProducer/blob/master/python/egmTreesSetup_cff.py#L78-L98
 */

template<typename T>
  auto tagMatchProducer(T &df, const char* s) {
  using namespace ROOT::VecOps;
  std::string flag(s);
  // trigger matching producer
  auto trgMatcher = [](RVec<int>& id, RVec<int>& filterbits , RVec<float>& eta_el , RVec<float>& phi_el , RVec<float>& eta_trg , RVec<float>& phi_trg , int& filter ) {

    // get combination
    auto comb = Combinations(eta_el,eta_trg); // electron-trig object pair
    const auto numComb = comb[0].size();
    RVec<int> matcher(eta_el.size(),1); // in case matching is not apply, all deemed pass

    for (size_t j=0 ; j < numComb ; j++){
      const auto iele = comb[0][j]; //electron
      const auto itrg = comb[1][j]; //trigobj

      //trigger object selection
      if (abs(id[itrg]) != 11) continue;
      //https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/NanoAOD/python/triggerObjects_cff.py#L35-L46
      if ( !Helper::bitdecoder(filterbits[itrg], filter) ) continue;
      const auto deltar = sqrt( pow(eta_el[iele] - eta_trg[itrg], 2) + pow(Helper::DeltaPhi(phi_el[iele], phi_trg[itrg]), 2));
      if (deltar > 0.3) matcher[iele] = 0;
      }
    return matcher;
  };

  // gen-matching producer
  auto genMatcher = [](RVec<float>& pt_el, RVec<float>& eta_el , RVec<float>& phi_el , RVec<int>& gen_pdgId , RVec<float>& pt_gen ,
                          RVec<float>& eta_gen , RVec<float>& phi_gen , RVec<int>& statusflag) {

      // get combination
      auto comb = Combinations(eta_el,eta_gen); // electron-gen object pair
      const auto numComb = comb[0].size();
      RVec<int> matcher(eta_el.size(),0); // in case matching is not apply, all deemed pass

      for (size_t i = 0 ; i < numComb ; i++){
        const auto iele = comb[0][i]; // ele
        const auto igen = comb[1][i]; // genpart

        //genpart selection
        //https://github.com/cms-analysis/EgammaAnalysis-TnPTreeProducer/blob/master/python/egmTreesSetup_cff.py#L83-L86
        if (abs(gen_pdgId[igen]) != 11) continue;
        if (pt_gen[igen] < 3) continue;
        if (abs(eta_gen[igen]) > 2.7) continue;
        // https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/NanoAOD/python/genparticles_cff.py#L48-L80
        if ( !Helper::bitdecoder(statusflag[igen],0) ) continue; // isPrompt
        if ( !Helper::bitdecoder(statusflag[igen],13) ) continue; // isLastCopy
        //genpart selection

        //https://github.com/cms-analysis/EgammaAnalysis-TnPTreeProducer/blob/master/python/egmTreesSetup_cff.py#L88-L98
        const auto deltar = sqrt( pow(eta_el[iele] - eta_gen[igen], 2) + pow(Helper::DeltaPhi(phi_el[iele], phi_gen[igen]), 2));
        const auto dpt_rel = fabs(pt_el[iele] - pt_gen[igen]) / pt_gen[igen];
        if (deltar > 0.2) continue; // Minimum deltaR for the match
        if (dpt_rel > 50.) continue; // Minimum deltaPt/Pt for the match
        // resolve ambiguity, pick lowest deltaR pair first , we dont need the gen information, so no need for now.
        matcher[iele] = 1;
      }
      return matcher;
  };

  auto out = df;
  if (flag=="trigger"){
    std::cout<<" >>> Matcher deployed : "<<flag<<" matching <<< "<<std::endl;
    out = df.Define("tagMatcher",trgMatcher,{"TrigObj_id","TrigObj_filterBits","Electron_eta","Electron_phi","TrigObj_eta","TrigObj_phi","bits"});
  }
  else if (flag=="gen"){
    std::cout<<" >>> Matcher deployed : "<<flag<<" matching <<< "<<std::endl;
    out = df.Define("tagMatcher",genMatcher,{"Electron_pt","Electron_eta","Electron_phi","GenPart_pdgId","GenPart_pt","GenPart_eta","GenPart_phi","GenPart_statusFlags"});
  }
  return out;
}

template <typename T>
auto tagProducer(T &df){
  //https://github.com/cms-analysis/EgammaAnalysis-TnPTreeProducer/blob/master/python/egmTreesSetup_cff.py#L30-L37
  return df.Define("isTag","tagCand==1 && tagMatcher==1");
}

/*************************************************** tnpPairingEleIDs ***************************************************/
/*
 * EDProducer + EDAnalyzer
 * tnpPairingEleIDs
 * https://github.com/cms-analysis/EgammaAnalysis-TnPTreeProducer/blob/master/python/egmTreesSetup_cff.py#L105-L111
 * pair collection
 */

template <typename T>
auto pairProducer(T &df) {
  using namespace ROOT::VecOps;
  auto tnpProducer = [](RVec<int>& isTag , RVec<float>& pt , RVec<float>& eta , RVec<float>& phi , RVec<float>& m ){

    auto comb = Combinations(isTag,isTag);
    const auto paircomb = comb[0].size();
    std::vector<std::pair<int,int>> pair_Idx;

    for(size_t i = 0 ; i < paircomb ; i++){
      const auto i1 = comb[0][i];
      const auto i2 = comb[1][i];

      if (i1==i2) continue;
      if (isTag[i1]!=1) continue; // first need to be tag
      TLorentzVector tot = Helper::VectorMaker( pt[i1] , eta[i1] , phi[i1] , m[i1] );
      TLorentzVector probe = Helper::VectorMaker( pt[i2] , eta[i2] , phi[i2] , m[i2] );
      tot+=probe;
      if ( tot.M() > 50 && tot.M() < 130 ) pair_Idx.push_back(std::make_pair(i1,i2));
    }
    //
    auto nTnP = pair_Idx.size();
    int ipair = -1, tidx = -1, pidx = -1; double randomness = -1.;
    if (nTnP==1) return std::vector<int>({pair_Idx[0].first , pair_Idx[0].second , static_cast<int>(nTnP) , ipair , static_cast<int>(randomness) });
    if (nTnP==0) return std::vector<int>({tidx , pidx , static_cast<int>(nTnP) , ipair , static_cast<int>(randomness) });

    // throw random number on selecting which pair
    TRandom3 rand = TRandom3();
    randomness = rand.Uniform(0,nTnP);
    ipair = static_cast<int>(randomness);
    tidx = pair_Idx[ipair].first;
    pidx = pair_Idx[ipair].second;

    return std::vector<int>({tidx , pidx , static_cast<int>(nTnP) , ipair , static_cast<int>(randomness) });

};

  return df
          .Define("tnpProducer", tnpProducer, {"isTag","Electron_pt","Electron_eta","Electron_phi","Electron_mass"})
          .Define("tag_Idx", "tnpProducer[0]")
          .Define("probe_Idx","tnpProducer[1]")
          .Define("nTnP","tnpProducer[2]")
          .Define("ipair","tnpProducer[3]")
          .Define("randomness","tnpProducer[4]")
          .Filter("(tag_Idx!=-1 && probe_Idx!=-1) && (tag_Idx!=probe_Idx)"," --> Filter invalid tnp pair")
          ;
}

/*
 * Probe WP definition
 *
 */
template <typename T>
auto probeWPProducer(T &df){
  using namespace ROOT::VecOps;
  auto leptonidx = [](RVec<int>& leptonwp , RVec<int>& leptonidx , int& pidx) {
    int lIdx=-1;
    for (size_t i=0 ; i< leptonidx.size() ; i++){
        //
        if ( leptonidx[i]== pidx ){
          lIdx=i;
          break;
        }
    }
    return leptonwp[lIdx];
  };

  return df
          .Define("passingMvaFall17V1Iso_WP90_SS",leptonidx,{"Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS","Lepton_electronIdx","probe_Idx"})
          .Define("passingMvaFall17V1Iso_WP90",leptonidx,{"Lepton_isTightElectron_mvaFall17V1Iso_WP90","Lepton_electronIdx","probe_Idx"})
          .Define("passingVeto","Electron_cutBased[probe_Idx]==1")
          .Define("passingLoose","Electron_cutBased[probe_Idx]==2")
          .Define("passingMedium","Electron_cutBased[probe_Idx]==3")
          .Define("passingTight","Electron_cutBased[probe_Idx]==4")
          .Define("passingMvaTTH","Electron_mvaTTH[probe_Idx]>0.7")
          ;
}

/*
 * Declare variables for analysis
 */

template <typename T>
auto DeclareVariables(T &df) {

  auto add_p4 = [](float pt, float eta, float phi, float mass)
    {
      return ROOT::Math::PtEtaPhiMVector(pt, eta, phi, mass);
    };

  auto pair = [](ROOT::Math::PtEtaPhiMVector& p4_1, ROOT::Math::PtEtaPhiMVector& p4_2)
    {
      return std::vector<float>( { float((p4_1+p4_2).Pt()) , float((p4_1+p4_2).Eta()) , float((p4_1+p4_2).Phi()) , float((p4_1+p4_2).M()) } );
    };

  return df
    .Define("tag_Ele_pt" ,"Electron_pt[tag_Idx]")
    .Define("tag_Ele_eta","Electron_eta[tag_Idx]")
    .Define("tag_Ele_phi","Electron_phi[tag_Idx]")
    .Define("tag_Ele_mass","Electron_mass[tag_Idx]")
    .Define("tag_Ele_q","Electron_charge[tag_Idx]")

    .Define("probe_Ele_pt" ,"Electron_pt[probe_Idx]")
    .Define("probe_Ele_eta","Electron_eta[probe_Idx]")
    .Define("probe_Ele_phi","Electron_phi[probe_Idx]")
    .Define("probe_Ele_mass","Electron_mass[probe_Idx]")
    .Define("probe_Ele_q","Electron_charge[probe_Idx]")

    .Define("tag_Ele",add_p4,{"tag_Ele_pt","tag_Ele_eta","tag_Ele_phi","tag_Ele_mass"})
    .Define("probe_Ele",add_p4,{"probe_Ele_pt","probe_Ele_eta","probe_Ele_phi","probe_Ele_mass"})
    .Define("pair" ,pair,{"tag_Ele","probe_Ele"})

    .Define("pair_pt" ,"pair[0]")
    .Define("pair_eta" ,"pair[1]")
    .Define("pair_phi" ,"pair[2]")
    .Define("pair_mass" ,"pair[3]")
    ;
}

/*
 * Add event weights
 */

template <typename T>
auto AddEventWeight(T &df, const std::string& lumi, const bool isMC) {

  std::string weights = (isMC==false) ? "METFilter_DATA" : lumi+"*XSWeight*puWeight*GenLepMatch2l*METFilter_MC"; //PromptGenLepMatch2l
  std::cout<<" >>> weights interpreted : "<<weights<<" <<< "<<std::endl;
  return df.Define( "weight", weights );
}

#endif
