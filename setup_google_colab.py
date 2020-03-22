#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pandas as pd

def download_file(url, file_path):
    print(url, file_path)
    if os.path.exists(file_path):
        os.remove(file_path)
    template = "wget '{}' -O '{}'"
    os.system(template.format(url, file_path))


def download_github_code(path):
    repo = 'kaggle/blob'
    branch = 'master'
    url = 'https://raw.githubusercontent.com/migai/{}/{}/{}'
    file_path = path.rsplit("/")[-1]
    download_file(url.format(repo, branch, path), file_path)


def download_github_with_pd_csv(path, df_name):
    repo = 'kaggle/blob'
    branch = 'master'
    url = 'https://raw.githubusercontent.com/migai/{}/{}/{}'
    file_path = path.rsplit("/")[-1]
    download_file(url.format(repo, branch, path), file_path)
	df_name = pd.read_csv(file_path)


def load_data_week1():
    download_github_code("week1_PandasBasics/grader.py")
	
	transactions = pd.DataFrame() 
	items = pd.DataFrame() 
	item_categories = pd.DataFrame() 
	shops = pd.DataFrame() 
	download_github_with_pd_csv("readonly/final_project_data/sales_train.csv.gz", transactions)
	download_github_with_pd_csv("readonly/final_project_data/items.csv", items)
	download_github_with_pd_csv("readonly/final_project_data/item_categories.csv", item_categories)
	download_github_with_pd_csv("readonly/final_project_data/shops.csv", shops)
	

def load_data_week2():
	return
