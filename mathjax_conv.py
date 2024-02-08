import io, sys

for fname in sys.argv[1:]:
    with io.open(fname) as f:
        result = f.read()
    result = result.replace('\\\\\\\\', '\\\\').replace('\\\\(', '$').replace('\\\\)', '$').replace('\\\\[', '$').replace('\\\\]', '$')
    with io.open(fname, 'w') as f:
        f.write("\n\pagebreak\n")
        f.write(result)