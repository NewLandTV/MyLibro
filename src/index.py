import pandas as pd
import path

kdc = pd.read_csv(path.join(path.data_dir, "KDC.idx"), sep="|").dropna()

def find_korean_decimal_classification(idx: str) -> str:
    """
    한국십진분류법에 해당하는 색인의 설명을 찾습니다.
    """
    return kdc.loc[kdc["index"] == idx, "description"].values[0]