#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""

import argparse
import logging
import wandb
import pandas as pd
import yaml
import os


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    artifact_local_path = run.use_artifact(args.input_artifact).file()

    logger.info(f"Downloaded input artifact to {artifact_local_path}")
    df_raw = pd.read_csv(artifact_local_path)

    # data cleaning refactored
    df = (
        df_raw.loc[
            df_raw["price"].between(args.min_price, args.max_price)
        ]  # Drop outliers
        .loc[df_raw["longitude"].between(-74.25, -73.50)]
        .loc[df_raw["latitude"].between(40.5, 41.2)]
        .assign(last_review=pd.to_datetime(df_raw["last_review"]))  # datetime
    )

    logger.info("Cleaned data for outliers")

    df.to_csv("clean_sample.csv", index=False)

    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file("clean_sample.csv")
    run.log_artifact(artifact)

    run.finish()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="Name of input artifact",
        required=True,
    )

    parser.add_argument(
        "--output_artifact",
        type=str,
        help="Name of output artifact",
        required=True,
    )

    parser.add_argument(
        "--output_type",
        type=str,
        help="Type of output, for example csv",
        required=True,
    )

    parser.add_argument(
        "--output_description",
        type=str,
        help="Describe what the output contains",
        required=True,
    )

    parser.add_argument(
        "--min_price",
        type=float,
        help="Cleaning: Ignore outliers with price < min_price",
        required=True,
    )

    parser.add_argument(
        "--max_price",
        type=float,
        help="Cleaning: Ignore outliers with price > max_price",
        required=True,
    )

    args = parser.parse_args()
    go(args)
