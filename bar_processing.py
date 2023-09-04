from tqdm import tqdm
import time

# Bar processing decorator
def bar_processing(func):
    def wrapper(*args, **kwargs):
        progress_bar = tqdm(total=100, dynamic_ncols=True)
        result = func(*args, **kwargs)
        progress_bar.close()
        return result
    return wrapper
