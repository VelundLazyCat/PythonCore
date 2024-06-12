
import re
source_file = 'source.txt'
output_file = 'output.txt'


def sanitize_file(source, output):

    with open(source, 'r') as fh:
        all_file = fh.read()

    all_file = re.sub(r'\d+', '', all_file)

    with open(output, 'w') as fh:
        fh.write(all_file)


sanitize_file(source_file, output_file)
