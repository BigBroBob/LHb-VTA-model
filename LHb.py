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

    model.state.v_n = []
    model.state.m = []
    model.state.h = []
    model.state.n = []
    model.state.h_T = []
    model.state.c =  []

    model.state.v_ast = []
    # concentration
    model.state.con_K_ext = []
    model.state.con_K_n = []
    model.state.con_K_ast = []
    model.state.con_Na_ext = []
    model.state.con_Na_n = []
    model.state.con_Na_ast = []

    return model

def alpha_m(v_n):
    return -(v_n+29.7)/10/(np.exp(-(v_n+29.7)/10)-1)
def alpha_n(v_n):
    return -(v_n+45.7)/100/(np.exp(-(v_n+45.7)/10)-1)
def alpha_h(v_n):
    return 0.07 * np.exp(-(v_n+48)/20)

def beta_m(v_n):
    return 4.0 * np.exp(-(v_n+54.7)/18)
def beta_n(v_n):
    return 0.125*np.exp(-(v_n+55.7)/80)
def beta_h(v_n):
    return 1.0/(np.exp(-(v_n+18)/10)+1)

def tau_m(v_n):
    return model.para.T_m / (alpha_m(v_n) + beta_m(v_n))
def tau_n(v_n):
    return model.para.T_n/(alpha_n(v_n)+beta_n(v_n))
def tau_h(v_n):
    return model.para.T_h/(alpha_h(v_n)+beta_h(v_n))

def m_inf(v_n):
    return alpha_m(v_n)/(alpha_m(v_n)+beta_m(v_n))
def n_inf(v_n):
    return alpha_n(v_n)/(alpha_n(v_n)+beta_n(v_n))
def h_inf(v_n):
    return alpha_h(v_n)/(alpha_h(v_n)+beta_h(v_n))
def h_T_inf(v_n):
    return 1.0/(1+np.exp(-model.para.gamma_h_T*(v_n-model.para.theta_h_T+model.para.v_sep)))

def m_T_inf(v_n):
    return 1.0/(1+np.exp(-model.para.gamma_m_T*(v_n-model.para.theta_m_T-model.para.v_sep)))

def v_nernst(con_ext,con_n):
    return model.para.R*model.para.T/model.para.F * np.log(con_ext/con_n)

def I_Na_n(v_n,m,h,con_Na_ext,con_Na_n):
    return model.para.g_Na * (m ** 3) * h * (v_n - v_nernst(con_Na_ext,con_Na_n))
def I_K_n(v_n,n,con_K_ext,con_K_n):
    return model.para.g_K * (n ** 4) * (v_n - v_nernst(con_K_ext,con_K_n))
def I_T(v_n,h_T):
    return model.para.g_T * m_T_inf(v_n)*h_T*(v_n-model.para.v_Ca)
def I_L_n(v_n):
    return model.para.g_L_n * (v_n-model.para.v_L_n)
def I_KCa(v_n,c,con_K_ext,con_K_n):
    return model.para.g_KCa * (c/(model.para.K_Ca+c))*(v_n-v_nernst(con_K_ext,con_K_n))

def I_Kir(v_ast,con_K_ext,con_K_ast):
    return model.para.g_Kir*\
            np.sqrt(con_K_ext)/(1+np.exp((v_ast+model.para.v_rest_ast-v_nernst(con_K_ext,con_K_ast)+model.para.vh)/model.para.vs))*\
            (v_ast+model.para.v_rest_ast-v_nernst(con_K_ext,con_K_ast))
def I_Kir_vess(v_ast,con_K_ast):
    return model.para.g_Kir_vess*\
            np.sqrt(model.para.con_K_vess)/(1+np.exp((v_ast+model.para.v_rest_ast-v_nernst(model.para.con_K_vess,con_K_ast)+model.para.vh)/model.para.vs))*\
            (v_ast+model.para.v_rest_ast-v_nernst(model.para.con_K_vess,con_K_ast))
def I_L_ast(v_ast):
    return model.para.g_L_ast * (v_ast-model.para.v_L_ast)

def i_pump_n(con_K_ext,con_Na_n):
    return model.para.i_max_n*((1+model.para.kmk/con_K_ext)**(-2))*((1+model.para.kna/con_Na_n)**(-3))
def i_pump_ast(con_K_ext,con_Na_ast):
    return model.para.i_max_ast*((1+model.para.kmk/con_K_ext)**(-2))*((1+model.para.kna/con_Na_ast)**(-3))

def I0(t):
    if t <= 500.0:
        I_t = 0
    elif t <= 1500.0:
        I_t = 3.15
    else:
        I_t = 0
    return model.para.I0 + I_t

def ode(x0,t):
    v_n,m,h,n,h_T,c,\
    v_ast,\
    con_K_ext,con_K_n,con_K_ast,\
    con_Na_ext,con_Na_n,con_Na_ast = x0

    dv_n = (-I_Na_n(v_n,m,h,con_Na_ext,con_Na_n)-I_K_n(v_n,n,con_K_ext,con_K_n)-I_L_n(v_n)-I_T(v_n,h_T)-I_KCa(v_n,c,con_K_ext,con_K_n)+I0(t))/model.para.C_n
    dm = (m_inf(v_n)-m)/tau_m(v_n)
    dh = (h_inf(v_n)-h)/tau_h(v_n)
    dn = (n_inf(v_n)-n)/tau_n(v_n)
    dh_T = (h_T_inf(v_n)-h_T)/model.para.tau_h_T
    dc = -model.para.k*model.para.g_T*m_T_inf(v_n)*h_T*(v_n-model.para.v_Ca)-model.para.k_Ca*c
    
    dv_ast = (-I_Kir(v_ast,con_K_ext,con_K_ast)-I_Kir_vess(v_ast,con_K_ast)-I_L_ast(v_ast))/model.para.C_ast
    
    dcon_K_ext = (I_K_n(v_n,n,con_K_ext,con_K_n)+I_KCa(v_n,c,con_K_ext,con_K_n))/model.para.F/model.para.Vol_ext+I_Kir(v_ast,con_K_ext,con_K_ast)/model.para.F/model.para.Vol_ext\
                    -2*i_pump_n(con_K_ext,con_Na_n)-2*i_pump_ast(con_K_ext,con_Na_ast)\
                    -model.para.g_eff_K_ext*(con_K_ext-model.para.con_K_ext_0)
    
    dcon_K_n = -(I_K_n(v_n,n,con_K_ext,con_K_n)+I_KCa(v_n,c,con_K_ext,con_K_n))/model.para.F/model.para.Vol_n\
                    +2*i_pump_n(con_K_ext,con_Na_n)*model.para.Vol_ext/model.para.Vol_n\
                    -model.para.g_eff_K_n*(con_K_n-model.para.con_K_n_0)
    
    dcon_K_ast = -I_Kir(v_ast,con_K_ext,con_K_ast)/model.para.F/model.para.Vol_ast-I_Kir_vess(v_ast,con_K_ast)/model.para.F/model.para.Vol_ast\
                    +2*i_pump_ast(con_K_ext,con_Na_ast)*model.para.Vol_ext/model.para.Vol_ast\
                    -model.para.g_eff_K_ast*(con_K_ast-model.para.con_K_ast_0)
    
    dcon_Na_ext = I_Na_n(v_n,m,h,con_Na_ext,con_Na_n)/model.para.F/model.para.Vol_ext\
                    +3*i_pump_n(con_K_ext,con_Na_n)+3*i_pump_ast(con_K_ext,con_Na_ast)\
                    -model.para.g_eff_Na_ext*(con_Na_ext-model.para.con_Na_ext_0)

    dcon_Na_n = -I_Na_n(v_n,m,h,con_Na_ext,con_Na_n)/model.para.F/model.para.Vol_n\
                    -3*i_pump_n(con_K_ext,con_Na_n)*model.para.Vol_ext/model.para.Vol_n\
                    -model.para.g_eff_Na_n*(con_Na_n-model.para.con_Na_n_0)
    
    dcon_Na_ast = -3*i_pump_ast(con_K_ext,con_Na_ast)*model.para.Vol_ext/model.para.Vol_ast\
                    -model.para.g_eff_Na_ast*(con_Na_ast-model.para.con_Na_ast_0)
    
    return [dv_n,dm,dh,dn,dh_T,dc,
                    dv_ast,
                    dcon_K_ext,dcon_K_n,dcon_K_ast,
                    dcon_Na_ext,dcon_Na_n,dcon_Na_ast]

model = init("parameter.json")
def simulation():    
    x0 = [model.para.v_n_init,m_inf(model.para.v_n_init),h_inf(model.para.v_n_init),n_inf(model.para.v_n_init),h_T_inf(model.para.v_n_init),0.0,
                    model.para.v_ast_init,
                    model.para.con_K_ext_init,model.para.con_K_n_init,model.para.con_K_ast_init,
                    model.para.con_Na_ext_init,model.para.con_Na_n_init,model.para.con_Na_ast_init]

    T = np.arange(0,model.para.sim.time_end,model.para.sim.time_step)
    
    sol = odeint(ode,x0,T)

    print('done')

    foldername = 'sim_LHb'
    os.makedirs(foldername)
    shutil.copy('parameter.json',foldername)
    np.savez(foldername+'/result.npz',
                v_n = sol[:,0],
                m = sol[:,1],
                h = sol[:,2],
                n = sol[:,3],
                h_T = sol[:,4],
                c = sol[:,5],
                v_ast = sol[:,6],
                con_K_ext = sol[:,7],
                con_K_n = sol[:,8],
                con_K_ast = sol[:,9],
                con_Na_ext = sol[:,10],
                con_Na_n = sol[:,11],
                con_Na_ast = sol[:,12]
    )

if __name__ == "__main__":
    simulation()