def to_indexed(source_file, output_file):

    with open(source_file, 'r') as fh:
        lines = fh.readlines()

    with open(output_file, 'w') as fh1:
        i = 0
        for line in lines:

            fh1.write(f'{i}: {line}')
            i += 1
