from pathlib import Path


ROOTDIR = Path(__file__).parents[1].resolve() / 'tools'
HOSTPYTHON = ROOTDIR / '..' / 'cpython' / 'build' / '3.7.0' / 'host'
TARGETPYTHON = ROOTDIR / '..' / 'cpython' / 'installs' / 'python-3.7.0'
DEFAULTCFLAGS = ''
DEFAULTLDFLAGS = ' '.join([
    '-O3',
    '-s', "BINARYEN_METHOD='native-wasm'",
    '-Werror',
    '-s', 'EMULATED_FUNCTION_POINTERS=1',
    '-s', 'EMULATE_FUNCTION_POINTER_CASTS=1',
    '-s', 'SIDE_MODULE=1',
    '-s', 'WASM=1',
    '--memory-init-file', '0'
    ])


def parse_package(package):
    # Import yaml here because pywasmcross needs to run in the built native
    # Python, which won't have PyYAML
    import yaml
    # TODO: Validate against a schema
    with open(package) as fd:
        return yaml.load(fd)
