import os
import random
import logging
import jsonpickle
from words import adjectives
from words import nouns


if __name__ != "__main__":
    from aws_xray_sdk.core import xray_recorder
    from aws_xray_sdk.core import patch_all

logger = logging.getLogger()
logger.setLevel(logging.INFO)

if __name__ != "__main__":
    patch_all()


def lambda_handler(event, context):
    logger.info(
        "## ENVIRONMENT VARIABLES\r" + jsonpickle.encode(dict(**os.environ))
    )
    logger.info("## EVENT\r" + jsonpickle.encode(event))
    logger.info("## CONTEXT\r" + jsonpickle.encode(context))

    adjective = random.choice(adjectives).strip().capitalize()
    noun = random.choice(nouns).strip().capitalize()

    return {"alias": f"{adjective}{noun}"}


if __name__ == "__main__":
    print(lambda_handler({}, {}))
