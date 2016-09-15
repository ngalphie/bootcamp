import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def ecdf(data):
    """
    Compute x, y values for an empirical distribution
    function
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) /len(x)
    return x, y


def bootstrap(data, func, size=1):
    """Function that draws bootstrap replicates
    Takes array of data, a function, size (default 1)
    Outputs the bs_replicates
    """
    #make empty array of replicates of the correct size
    bs_rep = np.empty(size)
    for i in range(size):
        bs_sample = np.random.choice(data, replace=True, size = len(data))
        bs_rep[i] = func(bs_sample)
    return bs_rep

def ci95(rep):
    """Function that takes in replicates and outputs the 95% confidence interval
    """
    return np.percentile(rep, [2.5, 97.5])

def cv(X):
    try:
        return np.std(X) / np.mean(X)
    except ZeroDivisionError:
        raise StatsError('mean is zero')

g_1973 = pd.read_csv('data/grant_1973.csv', delimiter=',', comment='#')
g_1975 = pd.read_csv('data/grant_1975.csv', delimiter=',', comment='#')
g_1987 = pd.read_csv('data/grant_1987.csv', delimiter=',', comment='#')
g_1991 = pd.read_csv('data/grant_1991.csv', delimiter=',', comment='#')
g_2012 = pd.read_csv('data/grant_2012.csv', delimiter=',', comment='#')

g_1973 = g_1973.rename(columns={'yearband':'year'})
g_1973.loc[:,'year'] = 1973

y_1975 = pd.DataFrame([1975]*len(g_1975), columns=['year'])
g_1975 = g_1975.join(y_1975)

y_1987 = pd.DataFrame([1987]*len(g_1987), columns=['year'])
g_1987 = g_1987.join(y_1987)

y_1991 = pd.DataFrame([1991]*len(g_1991), columns=['year'])
g_1991 = g_1991.join(y_1991)

y_2012 = pd.DataFrame([2012]*len(g_2012), columns=['year'])
g_2012 = g_2012.join(y_2012)

g_1973.columns = ['band', 'species', 'year', 'beak length (mm)', 'beak depth (mm)']
g_1975.columns = ['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']
g_1987.columns = ['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']
g_1991.columns = ['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']
g_2012.columns = ['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']

grantdf = pd.concat([g_1973, g_1975, g_1987, g_1991, g_2012], ignore_index=True)

# all_bands = grantdf.loc[:,'band']
# unique_bands =pd.DataFrame(np.unique(grantdf.loc[:,'band']))

grantdf = grantdf.drop_duplicates(['year', 'band'])

#d beak depths of fortis and scandens in 1987
plt.close()
plt.clf()
x1,y1 = ecdf(grantdf.loc[(grantdf['species']=='fortis') & (grantdf['year']==1987), 'beak depth (mm)'])
x2,y2 = ecdf(grantdf.loc[(grantdf['species']=='scandens') & (grantdf['year']==1987), 'beak depth (mm)'])
# bs_sample = np.random.choice(bd_1975, replace=True, size = len(bd_1975))
# x, y = ecdf(bs_sample)
plt.plot(x1, y1, marker='.', linestyle='none', alpha=0.5)
plt.plot(x2, y2, marker='.', linestyle='none', alpha=0.5)
# # plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none')
plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')
plt.legend(('fortis', 'scadens'), loc="lower right")
plt.margins(0.02)
plt.savefig('beak_depth_1987_fortis_scandens.pdf')

#d beak lengths of toris and scandens in 1987
plt.close()
plt.clf()
x3,y3 = ecdf(grantdf.loc[(grantdf['species']=='fortis') & (grantdf['year']==1987), 'beak length (mm)'])
x4,y4 = ecdf(grantdf.loc[(grantdf['species']=='scandens') & (grantdf['year']==1987), 'beak length (mm)'])
plt.plot(x3, y3, marker='.', linestyle='none', alpha=0.5)
plt.plot(x4, y4, marker='.', linestyle='none', alpha=0.5)
plt.xlabel('beak length (mm)')
plt.ylabel('ECDF')
plt.legend(('fortis', 'scadens'), loc="lower right")
plt.margins(0.02)
plt.savefig('beak_length_1987_fortis_scandens.pdf')

#e depth vs length 1973
plt.close()
plt.clf()
fortis_bl = grantdf.loc[(grantdf['species']=='fortis') & (grantdf['year']==1973), 'beak length (mm)']
scandens_bl = grantdf.loc[(grantdf['species']=='scandens') & (grantdf['year']==1973), 'beak length (mm)']
fortis_bd = grantdf.loc[(grantdf['species']=='fortis') & (grantdf['year']==1973), 'beak depth (mm)']
scandens_bd = grantdf.loc[(grantdf['species']=='scandens') & (grantdf['year']==1973), 'beak depth (mm)']
plt.plot(fortis_bl, fortis_bd, marker='.', linestyle='none', alpha=0.5, color='blue')
plt.plot(scandens_bl, scandens_bd, marker='.', linestyle='none', alpha=0.5, color='red')
plt.xlabel('beak length (mm)')
plt.ylabel('beak depth (mm)')
plt.legend(('fortis', 'scadens'), loc="lower right")
plt.margins(0.02)
plt.savefig('length_depth_1973_fortis_scandens.pdf')

#e depth vs length 1975
plt.close()
plt.clf()
fortis_bl = grantdf.loc[(grantdf['species']=='fortis') & (grantdf['year']==1975), 'beak length (mm)']
scandens_bl = grantdf.loc[(grantdf['species']=='scandens') & (grantdf['year']==1975), 'beak length (mm)']
fortis_bd = grantdf.loc[(grantdf['species']=='fortis') & (grantdf['year']==1975), 'beak depth (mm)']
scandens_bd = grantdf.loc[(grantdf['species']=='scandens') & (grantdf['year']==1975), 'beak depth (mm)']
plt.plot(fortis_bl, fortis_bd, marker='.', linestyle='none', alpha=0.5, color='blue')
plt.plot(scandens_bl, scandens_bd, marker='.', linestyle='none', alpha=0.5, color='red')
plt.xlabel('beak length (mm)')
plt.ylabel('beak depth (mm)')
plt.legend(('fortis', 'scadens'), loc="lower right")
plt.margins(0.02)
plt.savefig('length_depth_1975_fortis_scandens.pdf')

#e depth vs length 1987
plt.close()
plt.clf()
fortis_bl = grantdf.loc[(grantdf['species']=='fortis') & (grantdf['year']==1987), 'beak length (mm)']
scandens_bl = grantdf.loc[(grantdf['species']=='scandens') & (grantdf['year']==1987), 'beak length (mm)']
fortis_bd = grantdf.loc[(grantdf['species']=='fortis') & (grantdf['year']==1987), 'beak depth (mm)']
scandens_bd = grantdf.loc[(grantdf['species']=='scandens') & (grantdf['year']==1987), 'beak depth (mm)']
plt.plot(fortis_bl, fortis_bd, marker='.', linestyle='none', alpha=0.5, color='blue')
plt.plot(scandens_bl, scandens_bd, marker='.', linestyle='none', alpha=0.5, color='red')
plt.xlabel('beak length (mm)')
plt.ylabel('beak depth (mm)')
plt.legend(('fortis', 'scadens'), loc="lower right")
plt.margins(0.02)
plt.savefig('length_depth_1987_fortis_scandens.pdf')

#e depth vs length 1991
plt.close()
plt.clf()
fortis_bl = grantdf.loc[(grantdf['species']=='fortis') & (grantdf['year']==1991), 'beak length (mm)']
scandens_bl = grantdf.loc[(grantdf['species']=='scandens') & (grantdf['year']==1991), 'beak length (mm)']
fortis_bd = grantdf.loc[(grantdf['species']=='fortis') & (grantdf['year']==1991), 'beak depth (mm)']
scandens_bd = grantdf.loc[(grantdf['species']=='scandens') & (grantdf['year']==1991), 'beak depth (mm)']
plt.plot(fortis_bl, fortis_bd, marker='.', linestyle='none', alpha=0.5, color='blue')
plt.plot(scandens_bl, scandens_bd, marker='.', linestyle='none', alpha=0.5, color='red')
plt.xlabel('beak length (mm)')
plt.ylabel('beak depth (mm)')
plt.legend(('fortis', 'scadens'), loc="lower right")
plt.margins(0.02)
plt.savefig('length_depth_1991_fortis_scandens.pdf')

#e depth vs length 2012
plt.close()
plt.clf()
fortis_bl = grantdf.loc[(grantdf['species']=='fortis') & (grantdf['year']==2012), 'beak length (mm)']
scandens_bl = grantdf.loc[(grantdf['species']=='scandens') & (grantdf['year']==2012), 'beak length (mm)']
fortis_bd = grantdf.loc[(grantdf['species']=='fortis') & (grantdf['year']==2012), 'beak depth (mm)']
scandens_bd = grantdf.loc[(grantdf['species']=='scandens') & (grantdf['year']==2012), 'beak depth (mm)']
plt.plot(fortis_bl, fortis_bd, marker='.', linestyle='none', alpha=0.5, color='blue')
plt.plot(scandens_bl, scandens_bd, marker='.', linestyle='none', alpha=0.5, color='red')
plt.xlabel('beak length (mm)')
plt.ylabel('beak depth (mm)')
plt.legend(('fortis', 'scadens'), loc="lower right")
plt.margins(0.02)
plt.savefig('length_depth_2012_fortis_scandens.pdf')
