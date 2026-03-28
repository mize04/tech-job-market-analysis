import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np  
import seaborn as sns
df=pd.read_csv(r"C:\Users\USER\OneDrive\Desktop\mine\AI Job Market Dataset.csv")
print(df.head(10))
print(df.info())
new_df = df[(df['hiring_urgency']=="High") & (df['company_industry']=="Technology")]
print(new_df.head(10))
job_counts=new_df['job_title'].value_counts()
print(job_counts.head(10))
plt.figure()
wedges, texts,autotexts=plt.pie(job_counts.head(10),autopct='%1.1f%%', )
plt.legend(
    wedges,
    job_counts.head(10).index,
    title="Job_title",
    loc="center left",
    bbox_to_anchor=(1,0,0.5,1)
)
plt.title("Highest Tech jobs in demand")
plt.show()
plt.savefig("highest_tech_jobs_in_demand.png")
