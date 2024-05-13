import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("./medical_examination.csv")

# 2
df['overweight'] = np.where(df["weight"] / ((df["height"]/100) * (df["height"]/100)) > 25,1,0)

# 3
df["cholesterol"] = np.where(df["cholesterol"] == 1,0,1)
df["gluc"] = np.where(df["gluc"] == 1,0,1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars=["cardio"],value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    # 6
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index()
    df_cat = df_cat.rename(columns={0: "total"})
    #print(df_cat)
    
    # 8
    fig = sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar").fig



    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi'])
                     &(df['height'] >= df['height'].quantile(0.025))
                     &(df['height'] <= df['height'].quantile(0.975))
                     &(df['weight'] >= df['weight'].quantile(0.025))
                     &(df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    # 14
    fig, ax = plt.subplots(figsize=(12, 9))

    # 15
    ax = sns.heatmap(corr,mask=mask,vmax=0.4,square=True,fmt='.1f',annot=True)


    # 16
    fig.savefig('heatmap.png')
    return fig
