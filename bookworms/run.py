from cf_engine import cf_engine
import sys

new = cf_engine(user="37443397",min_books=4,match=3,kNN=30,test_size=0.5)
new.predict(new.train_data)