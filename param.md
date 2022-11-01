See the overview of model parameters and detailed definitions below.

## Parameters of LHb model

|Symbol|Value|Description|
|:-:|:-|:-|
|$C^{\rm N}$                        |30 pF                         |Membrane capacitance of LHb neuron|
|$C^{\rm A}$                        |1 pF                          |Membrane capacitance of LHb astrocyte|
|$T_{m}$                            |0.26                          |Relate parameter of $m$|
|$T_{n}$                            |0.26                          |Relate parameter of $n$|
|$T_{h}$                            |0.009                         |Relate parameter of $h$|
|$g_{\rm Na}$                       |120 mS                        |Conductance of LHb neuron sodium channel|
|$g_{\rm K}$                        |10 mS                         |Conductance of LHb neuron potassium channel|
|$g_{\rm T}$                        |0.6 mS                        |Conductance of LHb neuron T-type calcium channel|
|$g_{\rm KCa}$                      |1.2 mS                        |Conductance of LHb neuron calcium-dependent potassium channel|
|$g_{\rm L}$                        |0.25 mS                       |Conductance of LHb neuron leak channel|
|$g_{\rm Kir}$                      |12.5 mS                       |Conductance of LHb astrocyte Kir channel|
|$g_{\rm L}^{\rm A}$                |0.1 mS                        |Conductance of LHb astrocyte leak channel|
|$\gamma_{m_{\rm T}}$               |0.6                           |Relate parameter of $m_{\rm T}$|
|$\gamma_{h_{\rm T}}$               |-0.5                          |Relate parameter of $h_{\rm T}$|
|$\theta_{m_{\rm T}}$               |-64.5 mV                      |Voltage threshold of $m_{\rm T}$|
|$\theta_{h_{\rm T}}$               |-70 mV                        |Voltage threshold of $h_{\rm T}$|
|$v_{\rm sep}$                      |0mV                           |Voltage threshold offset of $m_{\rm T}$ and $h_{\rm T}$|
|$\tau_{h_T}$                       |22.222 ms                     |Relate parameter of $h_{\rm T}$|
|$E_{\rm Ca}^{\rm N}$               |130 mV                        |Calcium Nernst potential on LHb neuron membrane|
|$E_{\rm L}^{\rm N}$                |-50 mV                        |Leak Nernst potential on LHb neuron membrane|
|$E_{\rm L}^{\rm A}$                |-40 mV                        |Leak Nernst potential on LHb astrocyte membrane|
|$u_{\rm rest}^{\rm A}$             |-10 mV                        |Membrane rest potential of LHb astrocyte|
|$u_h$                              |178.46 mV                     |Relate parameter of Kir channel|
|$u_s$                              |119.47 mV                     |Relate parameter of Kir channel|
|$k$                                |0.001                         |Relate parameter of $c$|
|$k_{\rm Ca}$                       |0.044                         |Relate parameter of $c$|
|$K_{\rm Ca}$                       |1.0                           |Relate parameter of calcium-dependent potassium channel|
|$I_{\rm inp}$                      |3.15 uA                       |Dynamic stimulus input current|
|$R$                                |8.314 $\rm{J mol^{-1} K^{-1}}$|Ideal gas constant|
|$T$                                |308 K                         |Temperature|
|$F$                                |96.485 $\rm{kC mol^{-1}}$     |Faraday constant|
|$i_{\rm pump}^{\rm N}$             |0.12 $\rm{mM ms^{-1}}$        |Sodium-potassium pump rate of LHb neuron|
|$i_{\rm pump}^{\rm A}$             |0.12 $\rm{mM ms^{-1}}$        |Sodium-potassium pump rate of LHb astrocyte|
|$\delta_{\rm K}$                   |3 mM                          |Relate parameter of sodium-potassium pump|
|$\delta_{\rm Na}$                  |3 mM                          |Relate parameter of sodium-potassium pump|
|$V^{\rm N}$                        |10.8 pL                       |Volume of LHb neuron|
|$V^{\rm A}$                        |10.8 pL                       |Volume of LHb astrocyte|
|$V^{\rm ext}$                      |108 pL                        |Volume of LHb extracellular environment|
|$g_{{\rm eff}, {\rm K}}^{\rm N}$   |0.01 $\rm{ms^{-1}}$           |Effective flux rate of potassium in LHb neuron|
|$g_{{\rm eff}, {\rm K}}^{\rm ext}$ |0.1 $\rm{ms^{-1}}$            |Effective flux rate of potassium in LHb extracellular environment|
|$g_{{\rm eff}, {\rm K}}^{\rm A}$   |10 $\rm{ms^{-1}}$             |Effective flux rate of potassium in LHb astrocyte|
|$g_{{\rm eff}, {\rm Na}}^{\rm N}$  |0.01 $\rm{ms^{-1}}$           |Effective flux rate of sodium in LHb neuron|
|$g_{{\rm eff}, {\rm Na}}^{\rm ext}$|1 $\rm{ms^{-1}}$              |Effective flux rate of sodium in LHb extracellular environment|
|$g_{{\rm eff}, {\rm Na}}^{\rm A}$  |1 $\rm{ms^{-1}}$              |Effective flux rate of sodium in LHb astrocyte|
|$[{\rm K}]_{0}^{\rm N}$            |135 mM                        |Effective flux concentration of potassium in LHb neuron|
|$[{\rm K}]_{0}^{\rm ext}$          |3.5 mM                        |Effective flux concentration of potassium in LHb extracellular environment|
|$[{\rm K}]_{0}^{\rm N}$            |135 mM                        |Effective flux concentration of potassium in LHb astrocyte|
|$[{\rm Na}]_{0}^{\rm N}$           |12 mM                         |Effective flux concentration of sodium in LHb neuron|
|$[{\rm Na}]_{0}^{\rm ext}$         |144 mM                        |Effective flux concentration of sodium in LHb extracellular environment|
|$[{\rm Na}]_{0}^{\rm A}$           |7 mM                          |Effective flux concentration of sodium in LHb astrocyte|
|$[{\rm K}]^{\rm vess}$             |3.5 mM                        |Effective flux concentration of potassium in blood vessel|
|$u_{\rm init}^{\rm N}$             |-63.76 mV                     |Initial LHb neuron membrane potential|
|$u_{\rm init}^{\rm A}$             |-87.08 mV                     |Initial LHb astrocyte membrane potential|
|$[{\rm K}]_{\rm init}^{\rm N}$     |135.04 mM                     |Initial potassium concentration in LHb neuron|
|$[{\rm K}]_{\rm init}^{\rm ext}$   |3.34 mM                       |Initial potassium concentration in LHb extracellular environment|
|$[{\rm K}]_{\rm init}^{\rm A}$     |135 mM                        |Initial potassium concentration in LHb astrocyte|
|$[{\rm Na}]_{\rm init}^{\rm N}$    |11.16 mM                      |Initial sodium concentration in LHb neuron|
|$[{\rm Na}]_{\rm init}^{\rm ext}$  |145.95 mM                     |Initial sodium concentration in LHb extracellular environment|
|$[{\rm Na}]_{\rm init}^{\rm A}$    |7 mM                          |Initial sodium concentration in LHb astrocyte|

## Parameters of VTA model

|Symbol|Value|Description|
|:-:|:-|:-|
|$C^{\rm S}$                        |1 pF                           |Membrane capacitance of soma|
|$C^{\rm D}$                        |1 pF                           |Membrane capacitance of dendrite|
|$g_{\rm Na}^{\rm dop}$             |150 mS                         |Conductance of DAergic neuron sodium channel|
|$g_{\rm K,1}^{\rm dop}$            |0.4 mS                         |Conductance of DAergic neuron voltage-sensitive potassium channel|
|$g_{\rm K,2}^{\rm dop}$            |4 mS                           |Conductance of DAergic neuron spike-triggered (delayed rectifier) potassium channel|
|$g_{\rm Ca}^{\rm dop}$             |0.15 mS                        |Conductance of DAergic neuron calcium channel|
|$g_{\rm KCa}^{\rm dop}$            |0.3 mS                         |Conductance of DAergic neuron calcium-dependent potassium channel|
|$g_{\rm L}^{\rm dop}$              |0.05 mS                        |Conductance of DAergic neuron leak channel|
|$g_c$                              |0.3 mS                         |Conductance of soma-dendrite coupling|
|$g_{\rm GABA}$                     |0.2 mS                         |Conductance of GABA receptor|
|$k_1$                              |1                              |Relate parameter of DAergic neuron calcium-dependent potassium channel|
|$u_{h,{\rm K}}$                    |-10 mV                         |Relate parameter of DAergic neuron calcium-dependent potassium channel|
|$u_{s,{\rm K}}$                    |7 mV                           |Relate parameter of DAergic neuron calcium-dependent potassium channel|
|$E_{\rm Ca}^{\rm dop}$             |100 mV                         |Calcium Nernst potential on DAergic neuron membrane|
|$E_{\rm K}^{\rm dop}$              |-90 mV                         |Potassium Nernst potential on DAergic neuron membrane|
|$E_{\rm Na}^{\rm dop}$             |55 mV                          |Sodium Nernst potential on DAergic neuron membrane|
|$E_{\rm L}^{\rm dop}$              |-50 mV                         |Leak Nernst potential on DAergic neuron membrane|
|$E_{\rm GABA}^{\rm dop}$           |-80 mV                         |Nernst potential of GABA receptor|
|$N^D$                              |10                             |number of identical dendrites attached to soma|
|$\lambda$                          |0.05                           |Relate parameter of calcium flux between dendrite and soma|
|$F$                                |96.485 $\rm{kC mol^{-1}}$      |Faraday constant|
|$R^{\rm S}$                        |10 um                          |Soma radius|
|$R^{\rm D}$                        |0.5 um                         |Dendrite radius|
|$\theta^{\rm S}$                   |4                              |Relate parameter of soma calcium pump|
|$\theta^{\rm D}$                   |4                              |Relate parameter of dendrite calcium pump|
|$T_{n}^{\rm dop}$                  |1                              |Relate parameter of $n^{\rm dop}$|
|$T_{h}^{\rm dop}$                  |0.05                           |Relate parameter of $h^{\rm dop}$|
|$T_{s}^{\rm dop}$                  |1                              |Relate parameter of $s_{\infty}^{\rm dop}$|
|$\alpha_{\rm GABA}$                |0.5 $ms^{-1}$                  |Opening rate of GABA receptor|
|$\beta_{\rm GABA}$                 |0.18 $ms^{-1}$                 |Closing rate of GABA receptor|
|$[{\rm GABA}]_{\rm syn}$           |1 mM                           |GABA concentration of quantal discharges from LHb neuron into synaptic clefts|
|$u_{\rm init}^{\rm S}$             |-54.4 mV                       |Initial soma membrane potential|
|$u_{\rm init}^{\rm S}$             |-60 mV                         |Initial dendrite membrane potential|
|$[{\rm Ca}]_{\rm init}^{\rm S}$    |0.04 mM                        |Initial soma calcium concentration|
|$[{\rm Ca}]_{\rm init}^{\rm D}$    |0.04 mM                        |Initial dendrite calcium concentration|
|$n_{\rm init}^{\rm S}$             |0.17                           |Initial $n^{\rm S}$|
|$n_{\rm init}^{\rm D}$             |0.0025                         |Initial $n^{\rm D}$|
|$h_{\rm init}^{\rm S}$             |0.13                           |Initial $h^{\rm S}$|
|$h_{\rm init}^{\rm D}$             |1                              |Initial $h^{\rm D}$|
|$r_{\rm op,init}$                  |0.1                            |Initial $r_{\rm op}$|
