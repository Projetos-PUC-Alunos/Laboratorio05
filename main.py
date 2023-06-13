from query import query_runner
from os import environ
from sys import getsizeof
import pandas as pd


def main(interactions: int, token=None) -> None:
    if not token:
        if not 'GITHUB_TOKEN' in environ:
            token = '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'
        else:
            raise Exception(
                "You need to set the GITHUB_TOKEN environment variable or pass your token as an argument")
    configs = [
        { 'api': 'graphql', 'per_page': 5, 'type': 'REPOSITORY', },
        { 'api': 'rest', 'per_page': 5, 'type': 'REPOSITORY', },
        { 'api': 'graphql', 'per_page': 25, 'type': 'REPOSITORY', },
        { 'api': 'rest', 'per_page': 25, 'type': 'REPOSITORY', },
    ]
    df = pd.DataFrame(columns=['api', 'per_page', 'elapsed_time', 'body_size'])
    while interactions % len(configs) != 0: interactions += 1
    for i in range(interactions):
        print(f'Running query {i+1} of {interactions}')
        config = configs[i % len(configs)]
        body, elapsed_time = query_runner(config['api'], config['type'], config['per_page'], token)
        df = pd.concat([df, pd.DataFrame({
            'api': [config['api']],
            'per_page': [config['per_page']],
            'elapsed_time': [elapsed_time],
            'body_size': [getsizeof(str(body))],
        })])
    df.to_csv('out/results.csv', index=False)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='GitHub API')
    parser.add_argument('--interactions', '-i', type=int, help='Quantity of interactions for each API', default=10)
    parser.add_argument('--token', '-t', type=str, help='GitHub API token', default=None)
    args = parser.parse_args()
    main(1000)
