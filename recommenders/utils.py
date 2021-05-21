import pandas as pd

df_ccidf = pd.read_csv('resources/data/ccidf_only_db.csv').set_index('id')
df_tfidf = pd.read_csv('resources/data/tfidf_only_db.csv').set_index('id')
df_hybrid = pd.read_csv('resources/data/hybrid_db.csv').set_index('id')
df_paper = pd.read_csv('resources/data/paper_filtered_db.csv')

def get_recommendation(algo, filename, num_recom):
    if algo == 'CCIDF':
        M = df_ccidf
    elif algo == 'TFIDF':
        M = df_tfidf
    elif algo == 'Hybrid':
        M = df_hybrid
  # print(f'Below are {num_recom} recommendation from paper {title}')
    all_recom = M.loc[filename][M.index != filename].sort_values(ascending=False)[
        :num_recom]
  # print(df_raw[df_raw['filename']==filename]['abstract'].values[0])
    paper_infos = []
    for ids in all_recom.index:
        paper_info = {}
        paper = df_paper.loc[df_paper['id'] == ids]
        title = paper['title'].iloc[0]
        author = paper['author'].iloc[0]
        abstract = paper['abstract'].iloc[0]
        paper_info['title'] = title
        paper_info['author'] = author
        paper_info['abstract'] = abstract
        paper_infos.append(paper_info)
    return paper_infos

def load_paper_title():
    return df_paper['title'].tolist(), df_paper['id'].tolist()