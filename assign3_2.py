import pandas as pd
IIIT_LIBRARY={
    "subject":['math','ai','dbms','os','ai'],
    "bookauthor":['yash','yash','pranav','shaurya','mahesh'],
    "no_books":[2,1,2,3,7]
}
df = pd.DataFrame(IIIT_LIBRARY)
print(df.groupby("subject")['no_books'].sum())
