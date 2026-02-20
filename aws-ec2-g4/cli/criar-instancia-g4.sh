#!/bin/bash

aws ec2 run-instances \
    --image-id ami-xxxxxxxx \
    --instance-type g4dn.xlarge \
    --key-name minha-chave \
    --security-group-ids sg-xxxxxxxx \
    --subnet-id subnet-xxxxxxxx
