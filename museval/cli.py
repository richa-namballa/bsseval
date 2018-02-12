import sys
import argparse
from . import util
from . import eval_mus_dir
import musdb


def museval(inargs=None):
    """
    Commandline interface for museval evaluation tools
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'estimates_dir',
        type=str
    )

    parser.add_argument('-o', help='output_dir')

    parser.add_argument('--cpu', type=int, help='number of cpus', default=4)

    parser.add_argument(
        '-p', help='enable multiprocessing',
        action='store_true',
    )

    parser.add_argument(
        '--version', '-v',
        action='version',
        version='%%(prog)s %s' % util.__version__
    )

    args = parser.parse_args(inargs)
    mus = musdb.DB()

    if not args.o:
        output_dir = args.estimates_dir
    else:
        output_dir = args.o

    # evaluate an existing estimate folder with wav files
    eval_mus_dir(
        dataset=mus,  # instance of musdb
        estimates_dir=args.estimates_dir,  # path to estiamte folder
        output_dir=output_dir,  # set a folder to write eval json files
        parallel=args.p,
        cpus=args.cpu
    )


if __name__ == '__main__':
    museval(sys.argv[1:])
