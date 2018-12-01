# support functions for tests

def prepare_result(results):
    return str(sorted(results)).strip('][').replace("'","").replace("  "," ").replace(", ",",").strip()