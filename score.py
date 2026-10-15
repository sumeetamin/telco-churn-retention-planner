"""Score customers and emit a capacity-limited retention review queue."""
import argparse
from pathlib import Path
import joblib,numpy as np,pandas as pd
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument("--model",default="outputs/model.joblib");p.add_argument("--input",required=True);p.add_argument("--contact-share",type=float,default=.10);p.add_argument("--out",default="outputs/scored_customers.csv");a=p.parse_args()
 if not 0<a.contact_share<=1:raise SystemExit("--contact-share must be in (0,1].")
 b=joblib.load(a.model);d=pd.read_csv(a.input);features=b["features"];missing=[c for c in features if c not in d]
 if missing:raise SystemExit(f"Missing model features: {missing}")
 labels=np.asarray(b["classes"]);pos=b["positive_label"];ix=int(np.where(labels==pos)[0][0]);prob=b["pipeline"].predict_proba(d[features])[:,ix]
 k=max(1,int(np.ceil(len(d)*a.contact_share)));order=np.argsort(-prob);keep=[c for c in ["customerID","customer_id","id"] if c in d]
 result=pd.DataFrame({c:d.iloc[order[:k]][c].values for c in keep});result["churn_probability"]=prob[order[:k]];result["rank"]=np.arange(1,k+1)
 out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);result.to_csv(out,index=False);print(f"Created a {k:,}-row risk-ranked review queue at {out}. Risk is not a treatment effect.")
if __name__=="__main__":main()
