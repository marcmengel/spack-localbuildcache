import sys
import spack.config
from spack.extensions import localbuildcache as locext

description = "create buildcache of local packages in environment"
section = "environments"
level = "short"


def setup_parser(subparser):
    subparser.add_argument("--key", default=None, help="signing key for packges")
    subparser.add_argument(
        "--local",
        default=False,
        action="store_true",
        help="Restrict to packages local to this instance (not upstream)",
    )
    subparser.add_argument(
        "--not-bc",
        default=False,
        action="store_true",
        help="Restrict to packages not installed from a buildcache",
    )
    subparser.add_argument(
        "--dest",
        default="",
        help="destination url -- default is file:///environment_dir/bc",
    )


def localbuildcache(parser, args):
    locext.local_buildcache(args)
