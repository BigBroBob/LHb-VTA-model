from dotmap import DotMap
import json
import numpy as np
from scipy.integrate import odeint
import shutil
import os

def init(json_file):
    # load parameter
    with open(json_file,"rb") as f:
        para = json.load(f)
    para = DotMap(para)
    
    model = DotMap()
    model.para = para

    # soma
    model.state.v_so = []
    model.state.n_so = []
    model.state.h_so = []
    model.state.con_Ca_so = []

    # dendrite
    model.state.v_de = []
    model.state.n_de = []
    model.state.h_de = []
    model.state.con_Ca_de = []

    return model

def alpha_n(v):
    return -0.0032*(v+50.0)/(np.exp(-(v+50.0)/10.0)-1.0)
def beta_n(v):
    return 0.05*np.exp(-(v+10.0)/16.0)
def n_inf(v):
    return alpha_n(v)/(alpha_n(v)+beta_n(v))


def alpha_m(v):
    return -0.32*(v+31.0)/(np.exp(-(v+31.0)/4.0)-1.0)
def beta_m(v):
    return 4.0 * np.exp(-(v+54.7)/18)
def m_inf(v):
    return alpha_m(v)/(alpha_m(v)+beta_m(v))

def alpha_h(v):
    return 0.2*np.exp(-(v+47.0)/18.0)
def beta_h(v):
    return 25.0/(1.0+np.exp(-(v+24.0)/5.0))
def h_inf(v):
    return alpha_h(v)/(alpha_h(v)+beta_h(v))


def alpha_c(v):
    temp = np.abs(v+50.0) > 1e-5
    return temp * (-0.0032*(v+50.0)/(np.exp(-(v+50.0)/5.0)-1.0)) + (1-temp) * 0.016
def beta_c(v):
    return 0.05*np.exp(-(v+55.0)/40.0)
def c_inf(v):
    return alpha_c(v)/(alpha_c(v)+beta_c(v))

def g_Na1(v,h):
    return model.para.g_bar_Na1 * (m_inf(v)**3) * h
def g_K1(v):
    return model.para.g_bar_K1/(1.0+np.exp(-(v-model.para.v_Hk)/model.para.v_Sk))
def g_K2(n):
    return model.para.g_bar_K2 * n**4
def g_Ca1(v):
    return model.para.g_bar_Ca1 * c_inf(v)**4
def g_KCa1(u):
    return model.para.g_bar_KCa1 * u**4/(u**4+model.para.k1**4)
def g_NMDA(v,t_NMDA):
    return (t_NMDA*model.para.g_bar_NMDA+model.para.g_bar_NMDA_const)/(1.0+0.28*model.para.Mg*np.exp(-model.para.me*v))

def I_Ca(v):
    return g_Ca1(v)*(v-model.para.E_Ca)
def I_KCa(v,u):
    return g_KCa1(u)*(v-model.para.E_K)
def I_K1(v):
    return g_K1(v)*(v-model.para.E_K)
def I_K2(v,n):
    return g_K2(n)*(v-model.para.E_K)
def I_L(v):
    return model.para.g_L*(v-model.para.E_L)
def I_Na(v,h):
    return g_Na1(v,h)*(v-model.para.E_Na)
def I_so2de(v1,v2):
    return model.para.nd*model.para.g_c*(v1-v2)*(model.para.r1 * model.para.r2**2)/(model.para.r1**2+model.para.r2**2)
def I_de2so(v1,v2):
    return model.para.g_c*(v2-v1)*(model.para.r1**2 * model.para.r2)/(model.para.r1**2+model.para.r2**2)
def I_NMDA(v,t_NMDA):
    return g_NMDA(v,t_NMDA)*(v-model.para.E_NMDA)
def I_AMPA(v,t_NMDA):
    return model.para.g_AMPA*t_NMDA*(v-model.para.E_AMPA)
def I_GABA(v,r_op):
    return model.para.g_GABA_max*r_op*(v-model.para.E_GABA)

# LHb
foldername = 'sim_LHb'
f = np.load(foldername+'/result.npz')
v_LHb =  f['v_n']
GABA_LHb = np.zeros_like(v_LHb)

GABA_LHb = v_LHb >0

def ode(x0,t):
    v1,u1,n1,h1,\
        v2,u2,n2,h2,\
        r_op = x0

    I_t = 0.0
    t_NMDA = 0.0
    con_GABA = 0.0 

    t_order = np.floor(t/model.para.sim.time_step).astype(int)
    t_order = np.max([t_order,0])
    t_order = np.min([t_order,GABA_LHb.shape[0]-1])
    if GABA_LHb[t_order] == 1 :
        con_GABA = 1
    else:
        con_GABA = 0

    dv1 = (I_t - I_Ca(v1) - I_KCa(v1,u1) - I_K1(v1)-I_K2(v1,n1)-I_L(v1)-I_Na(v1,h1)-I_so2de(v1,v2))/model.para.C_so
    du1 = 2.0 * model.para.buf1/model.para.r1 * (-I_Ca(v1)/2.0/model.para.F-u1/model.para.t_C1)
    dn1 = model.para.tk * (alpha_n(v1)*(1.0-n1)-beta_n(v1)*n1)
    dh1 = model.para.th * (alpha_h(v1)*(1.0-h1)-beta_h(v1)*h1)

    dv2 = (-I_Ca(v2)-I_KCa(v2,u2)-I_K1(v2)-I_K2(v2,n2)-I_L(v2)-I_Na(v2,h2)-I_de2so(v1,v2)-I_NMDA(v2,t_NMDA)-I_AMPA(v2,t_NMDA)-I_GABA(v2,r_op))/model.para.C_de
    du2 = 2.0*model.para.buf1/model.para.r2*(-I_Ca(v2)/2.0/model.para.F-u2/model.para.t_C1)
    dn2 = model.para.tk * (alpha_n(v2)*(1.0-n2)-beta_n(v2)*n2)
    dh2 = model.para.th * (alpha_h(v2)*(1.0-h2)-beta_h(v2)*h2)

    dr_op = model.para.alpha_GABA*con_GABA*(1-r_op)-model.para.beta_GABA*r_op
    return [dv1,du1,dn1,dh1,   dv2,du2,dn2,dh2,      dr_op]

model = init("parameter.json")
def simulation():    
    x0 = [model.para.v1_init,model.para.u1_init,model.para.n1_init,model.para.h1_init,\
            model.para.v2_init,model.para.u2_init,model.para.n2_init,model.para.h2_init,\
            model.para.r_op_init]

    T = np.arange(0,model.para.sim.time_end,model.para.sim.time_step)
    
    sol = odeint(ode,x0,T)

    print('done')

    foldername = 'sim_VTA'
    os.makedirs(foldername)
    shutil.copy('parameter.json',foldername)
    np.savez(foldername+'/result.npz',
                v1 = sol[:,0],
                u1 = sol[:,1],
                n1 = sol[:,2],
                h1 = sol[:,3],
                v2 = sol[:,4],
                u2 = sol[:,5],
                n2 = sol[:,6],
                h2 = sol[:,7],
                r_op = sol[:,8]

    )

if __name__ == "__main__":
    simulation()