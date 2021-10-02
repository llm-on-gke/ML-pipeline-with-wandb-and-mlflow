#!/usr/bin/env python
"""
Performs basic cleaning on the data and save the results in Weights & Biases
"""
import argparse
import logging
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # YOUR CODE HERE     #
    ######################


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Cleans the data, drops missings and duplicates")


    parser.add_argument(
        "--input_artifact",
        type=## INSERT TYPE HERE: str, float or int,
        help=## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--output_artifact",
        type=## INSERT TYPE HERE: str, float or int,
        help=## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--output_type",
        type=## INSERT TYPE HERE: str, float or int,
        help=## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--output_description",
        type=## INSERT TYPE HERE: str, float or int,
        help=## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--min_price",
        type=## INSERT TYPE HERE: str, float or int,
        help=## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--max_price",
        type=## INSERT TYPE HERE: str, float or int,
        help=## INSERT DESCRIPTION HERE,
        required=True
    )

    args = parser.parse_args()

    go(args)
