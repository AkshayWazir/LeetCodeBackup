import math


def maxSubArray(a):
    m_s_f = -math.inf
    m_e_h = 0
    for i in range(len(a)):
        m_e_h = m_e_h + a[i]
        if m_s_f < m_e_h:
            m_s_f = m_e_h
        if m_e_h < 0:
            m_e_h = 0
    return m_s_f
