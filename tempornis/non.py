import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Your program description')
    parser.add_argument('--your_arg', type=str, help='Your argument description')
    args = parser.parse_args()
    return args
