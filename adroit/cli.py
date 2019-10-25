import argparse
import os
import sys
import logging

from .tester import AnsibleRoleTester, TestException, TestFailure

log = logging.getLogger(__name__)


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("role", nargs="+")
    parser.add_argument(
        "-b",
        "--base-name",
        default="adroit",
        help="Base of names for docker images and containers.",
    )
    parser.add_argument(
        "-d",
        "--default-image",
        default="debian:stretch",
        help="The image to base docker containers on by default.",
    )
    parser.add_argument(
        "-e", "--extra-vars", nargs="*", help="Extra variables to pass to Ansible."
    )
    parser.add_argument("-l", "--log-level", default="info")
    parser.add_argument(
        "-r",
        "--root-dir",
        default=os.getcwd(),
        help="Root directory of your Ansible setup.",
    )
    parser.add_argument(
        "-s",
        "--skip-build-images",
        action="store_true",
        help="Skip building of the base image(s).",
    )
    args = parser.parse_args()
    args.extra_vars = (
        dict(s.split("=", maxsplit=1) for s in args.extra_vars))
        if args.extra_vars
        else {}
    )
    return args


def main():
    args = parse_args()
    logging.basicConfig(
        format="%(asctime)s [%(levelname)8s] [%(name)s] %(message)s",
        level=logging.getLevelName(args.log_level.upper()),
    )

    try:
        tester = AnsibleRoleTester(
            args.root_dir,
            args.base_name,
            args.default_image,
            extra_vars=args.extra_vars,
        )

        for role in args.role:
            tester.check_role_exists(role)

        if not args.skip_build_images:
            tester.build_core_image()
            tester.build_base_image()

        for role in args.role:
            tester.test_role(role)
    except TestException:
        log.exception("exception while running tests")
        sys.exit(1)
    except TestFailure:
        log.exception("tests failed")
        sys.exit(2)


if __name__ == "__main__":
    main()
