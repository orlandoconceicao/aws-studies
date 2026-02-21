#!/bin/bash

aws stepfunctions create-state-machine \
  --name MeuWorkflow \
  --definition file://state-machine/workflow.json \
  --role-arn arn:aws:iam::CONTA:role/StepFunctionsRole
