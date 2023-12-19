import os
import json
from tqdm import tqdm

# =================
# == Basic Utils == 
# =================

def read_api_key(api_key:str=None) -> str:
    """Fetch the Riot Development API key. If None provided, it 
    will try to read the file ``apikey`` in the working directory.

    Parameters
    ----------
    api_key : :obj:`str`, optional
        The api key. 
    
    Returns
    -------
    str
        The api_key.

    Notes
    -----
        This function's main purpose is to hide your api key on
        public resources. You would want to store your api key
        in a file named ``apikey`` in the working directory, and 
        fetch your api key everytime through this function.
    """
    if not api_key:
        if not os.path.exists('apikey'):
            raise ValueError("Please provide valid Riot API key.")
        else:
            with open('apikey', 'r') as f:
                return f.read()
    else:
        return api_key

def write_messy_json(dic:dict, file:str) -> None:
    """Append a dictionary to a file. The file are organized
    line-by-line (each dict is a line).

    Parameters
    ----------
    dic : dict
        Any dictionary.
    file : str
        Name of file to append.
    """
    with open(file, 'a') as f:
        json.dump(dic, f)
        f.write('\n')


def clean_json(file:str, cutoff:int=16) -> list:
    """Clean a messy JSON file that store ``MatchTimelineDto`` s.
    Only retain matches that last longer than a specific cutoff.

    Parameters
    ----------
    file : str
        Messy file produced by write_messy_json(dic, file).
    cutoff : int
        Minimum minutes the matches must have. Defaults to 16.

    Returns
    -------
    dict
        The cleaned JSON content as a dictionary.
    """
    with open(file, 'r') as f:
        matches = []
        for i, line in enumerate(tqdm(f)):
            match = json.loads(line)
            frame_interval = match['info']['frameInterval']
            total_frame_num = len(match['info']['frames'])
            if total_frame_num < int(cutoff*60000/frame_interval):
                continue;
            matches += [match]
    print(f"There are in total {len(matches)} crawled matches " +
          f"longer than {cutoff} minutes.")
    with open(file, 'w') as f:  
        json.dump(matches, f)
    return matches

# =====================
# == Data Processing == 
# =====================

def json_data_mask(dic:dict) -> list:
    """Construct a list of keys that have dictionary as their
    corresponding value pair. The list acts as a mask for further
    cleaning.

    Parameters
    ----------
    dic: dict.
        Any dictionary.

    Returns
    -------
    list
        Keys of input dictionary which have dictionary as value. 
    """
    keys_to_remove = []
    for k,v in dic.items():
        if type(v) is dict:
            keys_to_remove = keys_to_remove + [k]
    return keys_to_remove