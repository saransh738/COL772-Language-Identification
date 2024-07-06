#!/bin/bash
TRAIN_COMMAND="python3 train.py"
TEST_COMMAND="python3 test.py"
if [ "$1" == "train" ]; then
    DATA_JSON="$2"
    SAVE_PATH="$3"
    $TRAIN_COMMAND $DATA_JSON $SAVE_PATH
fi
if [ "$1" == "test" ]; then
    MODEL_PATH="$2"
    DATA_JSON="$3"
    $TEST_COMMAND $MODEL_PATH $DATA_JSON
fi
