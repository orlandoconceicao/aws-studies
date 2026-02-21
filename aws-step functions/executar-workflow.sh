#!/bin/bash

aws stepfunctions start-execution \
  --state-machine-arn arn:aws:states:REGIAO:CONTA:stateMachine:MeuWorkflow
