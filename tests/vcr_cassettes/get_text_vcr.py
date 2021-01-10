import yaml
import vcr

def cassette_bianry_2_text(file_path):
    with open('./tests/vcr_cassettes/{}'.format(file_path), 'r') as f:
        doc = yaml.load(f)

    response = doc['interactions'][0]['response']
    decoded = vcr.filters.decode_response(response)
    print("\n--- The Body Contents of {} ---\n\n{}\n\n--- by 3n3a on GitHub ---\n\n\n".format(file_path, decoded['body']['string']))

if __name__ == "__main__":
    cassette_bianry_2_text("feed-users.yml")
    cassette_bianry_2_text("matches.yml")